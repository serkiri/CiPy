cipyPort = 8005

tpgp_jenkins_url = 'http://jenkins.pipe.tpgp.test02.aws.travisperkins.com:8080/'
tp_jenkins_url = 'http://jenkins.pipe.tp01.test02.aws.travisperkins.com:8080/'
cps_jenkins_url = 'http://jenkins.pipe.cps01.test02.aws.travisperkins.com:8080/'


jobs = [
    {
        'cipyPrettyName' : 'Unit Tests',
        'url' : 'http://jenkins.pipe.cloudshop-62.test02.aws.travisperkins.com:8080/job/Cloudshop_Unit_Test_And_Sonar/',
    },
    {
        'cipyPrettyName' : 'AAT TPGP',
        'url' : tpgp_jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
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
        'cipyPrettyName' : 'SIT TPGP',
        'url' : tpgp_jenkins_url + 'job/Cloudshop_Sit_MultiJob/',
    },
    {
        'cipyPrettyName' : 'AAT TP',
        'url' : tp_jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
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
        'url' : tp_jenkins_url + 'job/Cloudshop_Sit_MultiJob/',
    },
    {
        'cipyPrettyName' : 'AAT CPS',
        'url' : cps_jenkins_url + 'job/Cloudshop_Aat_MultiJob/',
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
        'cipyPrettyName' : 'SIT CPS',
        'url' : cps_jenkins_url + 'job/Cloudshop_Sit_MultiJob/',
    },
]