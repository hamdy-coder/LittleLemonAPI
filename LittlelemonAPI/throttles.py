from rest_framework.throttling import UserRateThrottle 

class FiveCallsPerMinute(UserRateThrottle): #makes ten calls per minute 
    scope = '5' 

    #---> goto settings ---> 

#TenCallsPerMinute(UserRateThrottle): #new throttle policy --> go  to settings
    #scope = 'ten' ---> then go to views and add 

    #from .throttles import TenCallsPerMinute 