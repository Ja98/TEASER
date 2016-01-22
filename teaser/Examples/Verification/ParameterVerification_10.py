# Created January 2016
# TEASER 4 Development Team

"""This module loads test case 10 given in VDI 6007-1 form a teaserXML file,
calculates all parameters and exports them as .txt. Differently to the other test cases,
we don't have the original parameter calculated by Rouvel. This test case defines the floor
as connected to an adjacent room with a fixed temperature. If you define the floor as ground floor,
TEASER doesn't allow you to define a coefficient of heat transfer on the outer surface (what makes
sense for a ground floor that is coupled to the ground). However, we need to define this coefficient,
so we handle this floor simply as a rooftop.
"""


def parameter_room10():
    """"First thing we need to do is to import our Project API module"""

    from teaser.Project import Project

    """We instantiate the Project class. The parameter load_data = True indicates
        that we load the XML data bases into our Project.
        This can take a few sec."""

    prj = Project(load_data=True)
    """We load the given test room defined in teaserXML-file"""

    prj.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room10.teaserXML')

    """Then we calculate all parameter with the calculation
    core 'vdi', that is exactly as defined in VDI 6007-1."""

    prj.calc_all_buildings('vdi')

    """After this, we can export our projects as .txt."""

    prj.export_parameters_txt()

if __name__ == '__main__':
    parameter_room10()
    print("That's it! :)")
