import IPython
import random

from copy import deepcopy

def secret_santa(data):
    n = len(data)
    indices = range(n)
    indicesb = deepcopy(indices)

    while any([indices[i] == indicesb[i] for i in range(n)]):
        random.shuffle(indicesb)

    #recip_number: assigned_person
    phone_person_map = {
            data[indices[i]]['phone']: make_msg(data[indicesb[i]], data[indices[i]])
            for i in range(n)
            }

    return phone_person_map


def make_msg(person_data, recip_data):
    msg = """Hey {0}, your person for secret santa is {1} and can be mailed to at {2}""".format(
            recip_data['name'], person_data['name'], person_data['address'])
    return msg

from twilio.rest import TwilioRestClient

def send_message(message, recipient_number):
    # Your Account Sid and Auth Token from twilio.com/user/account
    client = TwilioRestClient(account_sid, auth_token)

    #print "Would send following message to {0}: {1}".format(recipient_number, message)
    message = client.messages.create(body=message,
        to=recipient_number,    # Replace with your phone number
        from_="+13176536654") # Replace with your Twilio number
    print message.sid


if __name__ == '__main__':
  maps =  secret_santa(data)
  for k, v in maps.iteritems():
    send_message(v,k)

