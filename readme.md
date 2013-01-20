# hookstats

## gitstats/

[Parse Cloud Code](https://parse.com/docs/cloud_code_guide) setup. These functions can be used for everything from preprocessing query results to validations to making remote requests. The main thing I'm showing here (so far) is the ability to run tests against these function results. Parse's recommended method for testing is creating a secondary app to test against. The only disappointment I've had thus far is the inability to easily copy data from one parse app to another.

## hooks/

Example client side git hooks for posting data to Parse.

## parse-translator/

Google App Engine python application that takes a web hook payload and posts it to Parse. The best way to accomplish getting web hook data to Parse would be to create a [service hook](https://github.com/github/github-services) for Github that took the necessary Parse app id and REST API key. That said, it would only work for Github; Its open source alternative, Gitlab, does not yet have the ability for custom post-receive hooks.

This application needs to be configured for each repository, whose post-receive web hook gets set to its endpoint.

## app.js and index.html

Dashboard
