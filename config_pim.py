cipyPort = 8004

jenkins_url = 'http://10.0.151.19:8080/jenkins/'

jobs = [
    {
        'cipyPrettyName' : 'Unit Tests',
        'url' : jenkins_url + 'job/Cloudshop_UnitTest_And_SonarAnalysis/',
    },
    {
        'cipyPrettyName' : 'AAT',
        'url' : jenkins_url + 'job/Cloudshop_PIM_AAT_Multijob/',
        'subBuilds': [
            {
                'cipyPrettyName': 'Deploy',
                'jobName': 'Cloudshop_PIM_AAT_Deployment',
            },
            {
                'cipyPrettyName': 'BDD',
                'jobName': 'Cloudshop_PIM_AAT_BDD_Parallel',
            },
            {
                'cipyPrettyName': 'BDD Serial',
                'jobName': 'Cloudshop_PIM_AAT_BDD_Serial',
            },
            {
                'cipyPrettyName': 'BDD PES/TES',
                'jobName': 'Cloudshop_PIM_AAT_BDD_Serial_PES_TES',
            },
            {
                'cipyPrettyName': 'UI Cockpit',
                'jobName':'Cloudshop_PIM_AAT_UI_ProductCockPit_Desktop_Chrome',
            },
            {
                'cipyPrettyName': 'UI Lookup',
                'jobName':'Cloudshop_PIM_AAT_UI_ProductLookupPortal_Desktop_Chrome',
            },
            {
                'cipyPrettyName': 'UI Pim',
                'jobName':'Cloudshop_PIM_AAT_UI_PimSupplierPortal_Desktop_Chrome',
            },
        ]
    },
    {
        'cipyPrettyName' : 'SIT',
        'url' : jenkins_url + 'job/Cloudshop_PIM_SIT_Multijob',
        'subBuilds': [
            {
                'cipyPrettyName': 'Deploy',
                'jobName': 'Cloudshop_PIM_SIT_Deployment',
            },
            {
                'cipyPrettyName': 'BDD',
                'jobName': 'Cloudshop_PIM_SIT_BDD',
            },
        ]
    },
    {
        'cipyPrettyName' : 'UAT Deploy',
        'url' : jenkins_url + 'job/Cloudshop_PIM_UAT_Deploy/',
    },
]