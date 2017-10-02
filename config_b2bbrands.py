cipyPort = 8006

jenkins_url_bmx = 'http://jenkins.pipe.bmx01.test02.aws.travisperkins.com:8080/'
jenkins_url_ccf = 'http://jenkins.pipe.ccf01.test02.aws.travisperkins.com:8080/'
jenkins_url_kl = 'http://jenkins.pipe.kl01.test02.aws.travisperkins.com:8080/'


jobs = [
    {
        'cipyPrettyName' : 'Unit Tests',
        'url' : 'http://jenkins.pipe.cloudshop-62.test02.aws.travisperkins.com:8080/job/Cloudshop_Unit_Test_And_Sonar/',
    },
    {
        'cipyPrettyName' : 'AAT BMX prod',
        'url' : jenkins_url_bmx + 'job/Cloudshop_Aat_MultiJob/',
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
        'cipyPrettyName' : 'SIT BMX',
        'url' : jenkins_url_bmx + 'job/Cloudshop_Sit_MultiJob/',
    },
    {
        'cipyPrettyName' : 'AAT CCF prod',
        'url' : jenkins_url_ccf + 'job/Cloudshop_Aat_MultiJob/',
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
        'cipyPrettyName' : 'SIT CCF',
        'url' : jenkins_url_ccf + 'job/Cloudshop_Sit_MultiJob/',
    },
    {
        'cipyPrettyName' : 'AAT KL prod',
        'url' : jenkins_url_kl + 'job/Cloudshop_Aat_MultiJob/',
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
        'cipyPrettyName' : 'SIT KL',
        'url' : jenkins_url_kl + 'job/Cloudshop_Sit_MultiJob/',
    },

]