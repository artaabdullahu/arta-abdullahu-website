"""Publish dist/ to Hostinger over verified FTPS without deleting remote files."""

import ftplib
import hashlib
import os
from pathlib import Path
import ssl
import uuid


def deploy():
    root = Path(__file__).resolve().parents[1] / "dist"
    for name in ("index.html", "styles.css", "favicon.svg"):
        if not (root / name).is_file():
            raise RuntimeError(f"Missing deployment file: {name}")
    password = os.environ["HOSTINGER_FTP_PASSWORD"]
    context = ssl.create_default_context()
    # Some local Python installations do not have a configured CA bundle.
    try:
        import certifi
    except ImportError:
        pass
    else:
        context.load_verify_locations(certifi.where())

    with ftplib.FTP_TLS(context=context, timeout=45) as ftp:
        ftp.connect(os.environ.get("HOSTINGER_FTP_HOST", "185.210.234.150"), 21)
        # Hostinger's FTP certificate covers hstgr.io, rather than the IP.
        ftp.host = os.environ.get("HOSTINGER_FTP_TLS_NAME", "hstgr.io")
        ftp.auth()
        ftp.login(os.environ.get("HOSTINGER_FTP_USER", "u520185483.artaabdullahu.com"), password)
        ftp.prot_p()
        ftp.cwd(os.environ.get("HOSTINGER_FTP_DIR", "/public_html"))
        files = sorted(p for p in root.rglob("*") if p.is_file())
        # Publish the entry point after its assets have been uploaded.
        files.sort(key=lambda p: p.relative_to(root).as_posix() == "index.html")
        for local in files:
            if local.is_symlink():
                raise RuntimeError(f"Refusing to upload symlink: {local.name}")
            relative = local.relative_to(root).as_posix()
            parent = Path(relative).parent
            for directory in reversed(parent.parents):
                if directory.as_posix() != ".":
                    ensure_directory(ftp, directory.as_posix())
            if parent.as_posix() != ".":
                ensure_directory(ftp, parent.as_posix())
            temporary = relative + ".upload-" + uuid.uuid4().hex
            try:
                with local.open("rb") as stream:
                    ftp.storbinary("STOR " + temporary, stream)
                digest = hashlib.sha256()
                ftp.retrbinary("RETR " + temporary, digest.update)
                if digest.digest() != hashlib.sha256(local.read_bytes()).digest():
                    raise RuntimeError(f"Upload verification failed: {relative}")
                ftp.rename(temporary, relative)
            except Exception:
                try:
                    ftp.delete(temporary)
                except ftplib.all_errors:
                    pass
                raise
            print(f"Published and verified: {relative}")
        ftp.quit()


def ensure_directory(ftp, directory):
    try:
        ftp.mkd(directory)
    except ftplib.error_perm:
        current = ftp.pwd()
        ftp.cwd(directory)
        ftp.cwd(current)


if __name__ == "__main__":
    deploy()
