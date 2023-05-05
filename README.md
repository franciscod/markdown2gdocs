markdown2gdocs
---

## disclaimer

only `Heading 1` (`#`) and `Heading 2` (`##`) are supported.

tried supporting horizontal rules but there's no way to insert them from this api...

## how to

- make sure you have created a Google Cloud project and a service account.

- create a key for the service account and export it as json, save it to `service_account.json`.

- now, open a new Docs and share it with the service account. 

- take note of its document id! it looks a bit like this: `195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE`

- then for a test, run:

        make DOC_ID='<the document id of the one you just created>'
