cipyPort = 8004

jenkins_url = 'http://jenkins.pipe.pim.test01.aws.travisperkins.com:8080/'

jobs = [
    {
        'cipyPrettyName' : 'Unit Tests',
        'url' : 'http://jenkins.pipe.cloudshop.test01.aws.travisperkins.com:8080/job/Cloudshop_Unit_Test_And_Sonar/',
    },
    {
        'cipyPrettyName' : 'AAT',
        'url' : jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
        'parameters': {'name': 'FEATURE_SET', 'value': 'prodfeatures'},
        'subBuilds': [
            {
                'cipyPrettyName': 'AAT Deploy',
                'jobName': 'Cloudshop_Deploy',
            },
            {
                'cipyPrettyName': 'AAT BDD',
                'jobName': 'Cloudshop_Bdd',
                'phase': 'Parallel',
            },
            {
                'cipyPrettyName': 'AAT BDD Serial',
                'jobName': 'Cloudshop_Bdd',
                'phase': 'Serial',
            },
            {
                'cipyPrettyName': 'AAT UI Tests',
                'jobName':'Cloudshop_Ui_MultiJob',
            },
        ]
    },
    {
        'cipyPrettyName' : 'SIT',
        'url' : jenkins_url + 'job/Cloudshop_Sit_MultiJob/',
        'subBuilds': [
            {
                'cipyPrettyName': 'SIT Deploy',
                'jobName': 'Cloudshop_Deploy',
            },
            {
                'cipyPrettyName': 'SIT BDD',
                'jobName': 'Cloudshop_Bdd',
                'phase': 'Parallel',
            },
            {
                'cipyPrettyName': 'SIT BDD Serial',
                'jobName': 'Cloudshop_Bdd',
                'phase': 'Serial',
            },
            {
                'cipyPrettyName': 'SIT UI Tests',
                'jobName':'Cloudshop_Ui_MultiJob',
            },
        ]
    },
]