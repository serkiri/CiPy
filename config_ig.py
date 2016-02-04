cipyPort = 8002

jenkins_url = 'http://jenkins.pipe.igwc.test01.aws.travisperkins.com:8080/'

jobs = [
    {
        'cipyPrettyName' : 'Unit Tests',
        'url' : 'http://jenkins.pipe.cloudshop.test01.aws.travisperkins.com:8080/job/Cloudshop_Unit_Test_And_Sonar/',
    },
    {
        'cipyPrettyName' : 'AAT IG',
        'url' : jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
        'subBuilds': [
            {
                'cipyPrettyName': 'AAT Deploy',
                'jobName': 'Cloudshop_Deploy',
            },
            {
                'cipyPrettyName': 'AAT BDD Tests',
                'jobName': 'Cloudshop_Bdd',
            },
            {
                'cipyPrettyName': 'AAT UI Tests',
                'jobName':'Cloudshop_Desktop_MultiJob',
            },
        ]
    },
    {
        'cipyPrettyName' : 'SIT IG',
        'url' : jenkins_url + 'job/Cloudshop_Sit_MultiJob/',
        'subBuilds': [
            {
                'cipyPrettyName': 'SIT Deploy',
                'jobName': 'Cloudshop_Deploy',
            },
            {
                'cipyPrettyName': 'SIT BDD Tests',
                'jobName': 'Cloudshop_Bdd',
            },
        ]
    },
    {
        'cipyPrettyName' : 'UAT IG Deploy',
        'url' : jenkins_url + 'job/Cloudshop_Deploy_Uat/',
    },
]