#!/usr/bin/env python

import json
import sys
import urllib2

if __name__ == '__main__':

    # Check command line arguments
    if len(sys.argv) != 4:
        print "Invalid number of arguments!"
        print "Usage   : ", sys.argv[0], " <wunderground API key> <State> <City>"
        print "Example : ", sys.argv[0], " 123456789 GA San_Francisco"
        sys.exit(1)

    # Initialize
    apikey = sys.argv[1]
    state  = sys.argv[2]
    city   = sys.argv[3]

    # Get weather info from 'api.wunderground.com'
    url = 'http://api.wunderground.com/api/' + apikey + '/conditions/q/' + state + '/' + city + '.json'
    try:
        response = urllib2.urlopen(url).read()
    except urllib2.HTTPError, err:
        print "Error code : ", err.code
        sys.exit(1)
    except urllib2.URLError, err:
        print "Error : ", err.reason
        sys.exit(1)

    # Convert data to Json
    data = json.loads(response)

    # Retrieve today's predicted precipitation
    precip_today_metric = data['current_observation']['precip_today_metric']

    # Send a message to Slack Channel if the predicted precipitation is > 0
    if int(precip_today_metric) > 0:
        # Slack channel url
        url = 'https://hooks.slack.com/services/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'
        message = 'Predicted precipitation of ' + str(precip_today_metric) + ' mm today at ' + city + ", " + state
        data = json.dumps({'text': message})

        # Send a HTTP request
        try:
            req  = urllib2.Request(url, data, {'Content-Type': 'application/json'})
            f = urllib2.urlopen(req)
            response = f.read()
            print response
        except urllib2.HTTPError, err:
            print "Error code : ", err.code
        except urllib2.URLError, err:
            print "Error : ", err.reason
        finally:
            print "closing now"
            f.close()

