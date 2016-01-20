cipyPort = 8001

jenkins_url = 'http://jenkins.pipe.cps.test01.aws.travisperkins.com:8080/'

jobs = [
    {
        'cipyPrettyName' : 'Unit Tests',
        'url' : 'http://jenkins.pipe.cloudshop.test01.aws.travisperkins.com:8080/job/Cloudshop_Unit_Test_And_Sonar/',
    },
    {
        'cipyPrettyName' : 'AAT CPS',
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
                'jobName':'Cloudshop_UI_MultiJob',
            },
        ]
    },
    {
        'cipyPrettyName' : 'SIT CPS',
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
            {
                'cipyPrettyName': 'SIT UI Tests',
                'jobName':'Cloudshop_UI_MultiJob',
            },
        ]
    },
    {
        'cipyPrettyName' : 'UAT CPS Deploy',
        'url' : jenkins_url + 'job/Cloudshop_Deploy_Uat/',
    },
]