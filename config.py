jenkins_url = 'http://jenkins.pipe.tp.test01.aws.travisperkins.com:8080/'

jobs = [
    {
        'cipyPrettyName' : 'AAT prodfeatures',
        'url' : jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
        'parameters': {'name': 'FEATURE_SET', 'value': 'prodfeatures'},
    },
    {
        'cipyPrettyName' : 'AAT allfeatures',
        'url' : jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
        'parameters': {'name': 'FEATURE_SET', 'value': 'allfeatures'},
    },
    {
        'cipyPrettyName' : 'SIT',
        'url' : jenkins_url + 'job/Cloudshop_Sit_MultiJob/',
    },
]