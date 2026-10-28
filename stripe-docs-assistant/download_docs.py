import pathlib, ssl, urllib.request
import certifi

ctx = ssl.create_default_context(cafile=certifi.where())
out = pathlib.Path("data"); out.mkdir(exist_ok=True)
for url in pathlib.Path("urls.txt").read_text().split():
    md_url = url if url.endswith(".md") else url.rstrip("/") + ".md"
    name = md_url.split("docs.stripe.com/")[-1].replace("/", "_")
    try:
        data = urllib.request.urlopen(md_url, context=ctx).read()
        out.joinpath(name).write_bytes(data)
        print("saved", name)
    except Exception as e:
        print("skipped", url, "-", e)