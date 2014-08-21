msisdn-cli
==========

This little CLI tool let you validate both MT and MOMT flow using
MSISDN server.

To start a MT Flow::

    msisdn-cli -H https://msisdn.services.mozilla.com \
        -c 310 -n +1xxxxxxxxxxx

To start a MOMT Flow::

    msisdn-cli -H https://msisdn.services.mozilla.com -c 310

You can also create a certificate to then try to register on a Service
Provider such as Loop.

To do so add an --audience parameter and a --login-endpoint you can
also provide some --data or --json to be POST with your registration
request::

    msisdn-cli -H https://msisdn.services.mozilla.com -c 310 -n +1xxxxxxxxxxx \
               --audience https://loop.services.mozilla.com
               --login-endpoint https://loop.services.mozilla.com/registration
               --json '{"simplePushURL": "http://httpbin.org/deny"}'

If you want you can just display the cURL command using --dry-run::

    msisdn-cli -H https://msisdn.services.mozilla.com -c 310 -n +1xxxxxxxxxxx \
               --audience https://loop.services.mozilla.com
               --login-endpoint https://loop.services.mozilla.com/registration
               --json '{"simplePushURL": "http://httpbin.org/deny"}' --dry-run

The msisdn-cli script will then build you an assertion and write
down a curl command to run to make sure it works.

You can also use the -v, --verbose command to display the assertion.

You should get a 200 OK status code with a Hawk-Session-Token header.

If not, here are the error messages you can get:

- "Certificate expired": you play too long with this curl command,
                         ask for a new certificate

- "Invalid audience":    The Service Provider doesn't accept this audience
                         It can be either a misconfiguration on the server or
                         you trying the assertion to a wrong server.

- "Issuer not trusted":  The MSISDN server that generate your certificate
                         is not trusted on this Service Provider.
                         It can be either a misconfiguration or
                         you trying the assertion to a wrong server.

- Something else? Please make a PR to add it here.

Don't forget to use :code:`msisdn-cli -h` to get more help.


INSTALL
-------

::

    make install
    source .venv/bin/activate
