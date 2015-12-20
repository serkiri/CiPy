jenkins_url = 'http://jenkins.pipe.tp.test01.aws.travisperkins.com:8080/'

jobs = [
    {
        'cipyPrettyName' : 'AAT prodfeatures',
        'url' : jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
        'parameters': {'name': 'FEATURE_SET', 'value': 'prodfeatures'},
        'subBuilds': [
            'Cloudshop_Deploy',
            'Cloudshop_Bdd',
            'Cloudshop_Ui_MultiJob',
        ]
    },
    {
        'cipyPrettyName' : 'AAT allfeatures',
        'url' : jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
        'parameters': {'name': 'FEATURE_SET', 'value': 'allfeatures'},
        'subBuilds': [
            'Cloudshop_Deploy',
            'Cloudshop_Bdd',
            'Cloudshop_Ui_MultiJob',
        ]
    },
    {
        'cipyPrettyName' : 'SIT',
        'url' : jenkins_url + 'job/Cloudshop_Sit_MultiJob/',
    },
]