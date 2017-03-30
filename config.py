cipyPort = 8000

jenkins_url = 'http://jenkins.pipe.tp.test02.aws.travisperkins.com:8080/'
jenkins_url_cps = 'http://jenkins.pipe.cps.test02.aws.travisperkins.com:8080/'

jobs = [
    {
        'cipyPrettyName' : 'Unit Tests',
        'url' : 'http://jenkins.pipe.cloudshop.test02.aws.travisperkins.com:8080/job/Cloudshop_Unit_Test_And_Sonar/',
    },
    {
        'cipyPrettyName' : 'AAT TP prod',
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
        'cipyPrettyName' : 'SIT TP',
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
    {
        'cipyPrettyName' : 'AAT CPS prod',
        'url' : jenkins_url_cps + 'job/Cloudshop_Aat_MultiJob/',
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
                'jobName':'Cloudshop_UI_MultiJob',
            },
        ]
    },
    {
        'cipyPrettyName' : 'SIT CPS',
        'url' : jenkins_url_cps + 'job/Cloudshop_Sit_MultiJob/',
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
                'jobName':'Cloudshop_UI_MultiJob',
            },
        ]
    },
    {
        'cipyPrettyName' : 'Code Freeze',
        'url' : 'http://epuakhaw0602.kyiv.epam.com:8080/job/b2bCodeFreeze/',
    },
]