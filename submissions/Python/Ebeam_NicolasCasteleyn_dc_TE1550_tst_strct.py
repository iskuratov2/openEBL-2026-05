# Copyright (C) 2020-2025 Luceda Photonics


from siepic import all as pdk
from ipkiss3 import all as i3
from ipkiss.technology import get_technology
import numpy as np

TECH = get_technology()


class dc_TE1550_tst_strct(i3.Circuit):
    bend_radius = i3.PositiveNumberProperty(default=5.0, doc="Bend radius of the waveguides")

    fgc = i3.ChildCellProperty(doc="PCell for the fiber grating coupler")
    dir_coupler = i3.ChildCellProperty(doc="PCell for the directional coupler")
    terminator = i3.ChildCellProperty(doc="PCell for the terminator")

    delay_length = i3.PositiveNumberProperty(default=60.0, doc="length difference between the arms of the MZI")

    def _default_fgc(self):
        return pdk.EbeamGCTE1550()

    def _default_dir_coupler(self):
        return pdk.EbeamBDCTE1550()

    def _default_terminator(self):
        return pdk.EbeamTerminatorTE1550()

    def _default_specs(self):
        specs = [
            i3.Inst(["fgc_1", "fgc_2", "fgc_3"], self.fgc),
            i3.Inst("dc", self.dir_coupler),
            i3.Inst("terminator", self.terminator),
        ]

        fgc_spacing_y = 127.0
        specs += [
            i3.Place("fgc_1:opt1", (0, 0)),
            i3.Place("fgc_2:opt1", (0.0, fgc_spacing_y), relative_to="fgc_1:opt1"),
            i3.Place("fgc_3:opt1", (0.0, fgc_spacing_y), relative_to="fgc_2:opt1"),
            i3.Place("dc:opt1", (20.0, -40.0), angle=90, relative_to="fgc_3:opt1"),
            i3.Place("terminator:opt1", (0.0, 0.0), angle=-90, relative_to="dc:opt1"),
            i3.Join("terminator:opt1","dc:opt1"),
        ]

        specs += [
            i3.ConnectManhattan(
                [
                    ("fgc_3:opt1", "dc:opt2", "fgc_3_opt1_to_dc_opt2"),
                    ("dc:opt4", "fgc_2:opt1", "dc_opt4_to_fgc_2_opt1"),
                    ("dc:opt3", "fgc_1:opt1", "dc_opt3_to_fgc_1_opt1"),
                ]
            ),

        ]
        return specs

    def get_connector_instances(self):
        lv_instances = self.get_default_view(i3.LayoutView).instances
        return [
            lv_instances["fgc_3_opt1_to_dc_opt2"],
            lv_instances["dc_opt4_to_fgc_2_opt1"],
            lv_instances["dc_opt3_to_fgc_1_opt1"],
        ]

    def _default_exposed_ports(self):
        exposed_ports = {
            "fgc_3:fib1": "in",
            "fgc_2:fib1": "out1",
            "fgc_1:fib1": "out2",
        }
        return exposed_ports
class dc_TE1550_cross_tst_strct(i3.Circuit):
    bend_radius = i3.PositiveNumberProperty(default=5.0, doc="Bend radius of the waveguides")

    fgc = i3.ChildCellProperty(doc="PCell for the fiber grating coupler")
    dir_coupler = i3.ChildCellProperty(doc="PCell for the directional coupler")
    terminator = i3.ChildCellProperty(doc="PCell for the terminator")

    delay_length = i3.PositiveNumberProperty(default=60.0, doc="length difference between the arms of the MZI")

    def _default_fgc(self):
        return pdk.EbeamGCTE1550()

    def _default_dir_coupler(self):
        return pdk.EbeamBDCTE1550()

    def _default_terminator(self):
        return pdk.EbeamTerminatorTE1550()

    def _default_specs(self):
        specs = [
            i3.Inst(["fgc_1", "fgc_2"], self.fgc),
            i3.Inst("dc", self.dir_coupler),
            i3.Inst(["terminator_1", "terminator_2"], self.terminator),
        ]

        fgc_spacing_y = 127.0
        specs += [
            i3.Place("fgc_1:opt1", (0, 0)),
            i3.Place("fgc_2:opt1", (0.0, fgc_spacing_y), relative_to="fgc_1:opt1"),
            i3.Place("dc:opt1", (20.0, -40.0), angle=90, relative_to="fgc_2:opt1"),
            i3.Place("terminator_1:opt1", (0.0, 0.0), angle=-90, relative_to="dc:opt1"),
            i3.Join("terminator_1:opt1","dc:opt1"),
            i3.Place("terminator_2:opt1", (0.0, 0.0), angle=90, relative_to="dc:opt4"),
            i3.Join("terminator_2:opt1","dc:opt4"),
        ]

        specs += [
            i3.ConnectManhattan(
                [
                    ("dc:opt2", "fgc_2:opt1", "dc_opt2_to_fgc_2_opt1"),
                    ("dc:opt3", "fgc_1:opt1", "dc_opt3_to_fgc_1_opt1"),
                ]
            ),

        ]
        return specs

    def get_connector_instances(self):
        lv_instances = self.get_default_view(i3.LayoutView).instances
        return [
            lv_instances["dc_opt2_to_fgc_2_opt1"],
            lv_instances["dc_opt3_to_fgc_1_opt1"],
        ]

    def _default_exposed_ports(self):
        exposed_ports = {
            "fgc_2:fib1": "in",
            "fgc_1:fib1": "out",
        }
        return exposed_ports
class dc_TE1550_bar_tst_strct(i3.Circuit):
    bend_radius = i3.PositiveNumberProperty(default=5.0, doc="Bend radius of the waveguides")

    fgc = i3.ChildCellProperty(doc="PCell for the fiber grating coupler")
    dir_coupler = i3.ChildCellProperty(doc="PCell for the directional coupler")
    terminator = i3.ChildCellProperty(doc="PCell for the terminator")

    delay_length = i3.PositiveNumberProperty(default=60.0, doc="length difference between the arms of the MZI")

    def _default_fgc(self):
        return pdk.EbeamGCTE1550()

    def _default_dir_coupler(self):
        return pdk.EbeamBDCTE1550()

    def _default_terminator(self):
        return pdk.EbeamTerminatorTE1550()

    def _default_specs(self):
        specs = [
            i3.Inst(["fgc_1", "fgc_2"], self.fgc),
            i3.Inst("dc", self.dir_coupler),
            i3.Inst(["terminator_1", "terminator_2"], self.terminator),
        ]

        fgc_spacing_y = 127.0
        specs += [
            i3.Place("fgc_1:opt1", (0, 0)),
            i3.Place("fgc_2:opt1", (0.0, fgc_spacing_y), relative_to="fgc_1:opt1"),
            i3.Place("dc:opt1", (20.0, -40.0), angle=90, relative_to="fgc_2:opt1"),
            i3.Place("terminator_1:opt1", (0.0, 0.0), angle=-90, relative_to="dc:opt1"),
            i3.Join("terminator_1:opt1","dc:opt1"),
            i3.Place("terminator_2:opt1", (0.0, 0.0), angle=90, relative_to="dc:opt3"),
            i3.Join("terminator_2:opt1","dc:opt3"),
        ]

        specs += [
            i3.ConnectManhattan(
                [
                    ("dc:opt2", "fgc_2:opt1", "dc_opt2_to_fgc_2_opt1"),
                    ("dc:opt4", "fgc_1:opt1", "dc_opt4_to_fgc_1_opt1"),
                ]
            ),

        ]
        return specs

    def get_connector_instances(self):
        lv_instances = self.get_default_view(i3.LayoutView).instances
        return [
            lv_instances["dc_opt2_to_fgc_2_opt1"],
            lv_instances["dc_opt4_to_fgc_1_opt1"],
        ]

    def _default_exposed_ports(self):
        exposed_ports = {
            "fgc_2:fib1": "in",
            "fgc_1:fib1": "out",
        }
        return exposed_ports

dut = dc_TE1550_tst_strct
dut = dc_TE1550_cross_tst_strct
dut = dc_TE1550_bar_tst_strct
enable_visualize = False

if __name__ == "__main__":
    # Layout
    dut = dut(
        name="dc_tst",
        delay_length=60.0,
        bend_radius=5.0,
    )
    dut_layout = dut.Layout()
    if enable_visualize:
        dut_layout.visualize(annotate=True)
        dut_layout.visualize_2d()

    dut_layout.write_gdsii("dc_TE1550_tst_strct.gds")
