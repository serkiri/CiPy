cipyPort = 8003

jenkins_url = 'http://jenkins.pipe.soa.test02.aws.travisperkins.com:8080/'

jobs = [
    {
        'cipyPrettyName' : 'MDM On Push',
        'url' : jenkins_url + 'job/Branch-Entity-Service_OnPush_Master/',
    },
    {
        'cipyPrettyName' : 'MDM Deploy SIT',
        'url' : jenkins_url + 'job/Branch-Entity-Service_Deploy_ECS_SIT/',
    },
    {
        'cipyPrettyName' : 'MDM SIT',
        'url' : jenkins_url + 'job/MDM_SIT/',
    },
    {
        'cipyPrettyName' : 'MDM Deploy UAT',
        'url' : jenkins_url + 'job/Branch-Entity-Service_Deploy_ECS_UAT/',
    },
]