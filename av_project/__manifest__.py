{
    'name': 'Project Purchase Approval',
    'depends': ['base' , 'project' , 'hr'],
    'author': 'Glo',
    'data': [
        # Security data

        'security/ir.model.access.csv',
        'security/res_groups.xml',

        #Views data
        'views/project_view.xml',
        'views/department_view.xml'
    ] ,

}