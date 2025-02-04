{
    'name': 'Project Purchase Approval',
    'depends': ['base' , 'project' , 'purchase' , 'hr'],
    'author': 'Glo',
    'data': [
        # Security data

        'security/ir.model.access.csv',
        'security/res_groups.xml',

        #Views data
        'views/ppa_project_view.xml',
    ] ,

}