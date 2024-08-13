
from yangify.translator import Translator, TranslatorData, unneeded
from vht.common.translators.VHT_ip_cfg.ip import *
from vht.helper import *
from pprint import pprint


class Ip_Route_IpRouteStatic_Impl(Ip_Route_IpRouteStatic):
    class Yangify(Ip_Route_IpRouteStatic.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_IpRouteStatic_Impl.Yangify, self).__init__(*args, **kwargs)
            self.cli_fmt      = "ip route {prefix}/{mask} {out} tag {tag} description {description}"
            self.undo_cli_fmt = "no ip route {prefix}/{mask} {out}"

        def extract_cli_data2(self, cli_data):
            if 'next_hop_ip_add' in cli_data:
                cli_data['out'] = cli_data['next_hop_ip_add']
            elif 'out_if' in cli_data:
                cli_data['out'] = cli_data['out_if']
            cli_data['tag'] = cli_data['tag']
            cli_data['description'] = cli_data['description']

    def __init__(self, *args, **kwargs):
        super(Ip_Route_IpRouteStatic_Impl, self).__init__(*args, **kwargs)

class Ip_Route_Vrf_Impl1(Ip_Route_Vrf):
    class Yangify(Ip_Route_Vrf.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_Vrf_Impl1.Yangify, self).__init__(*args, **kwargs)
            self.cli_fmt = "route vrf {name}"
            self.cli_exit = None

        @debug_function(log_exit=True, log_return=True)
        def _stringify_add_to_list_command1(self, element):
            command = self.cli_fmt.format(**element)
            return command

    def __init__(self, *args, **kwargs):
        super(Ip_Route_Vrf_Impl1, self).__init__(*args, **kwargs)
        
class Ip_Route_Vrf_IpRouteStatic_Impl(Ip_Route_Vrf_IpRouteStatic, Ip_Route_Vrf_Impl1):
    class Yangify(Ip_Route_Vrf_IpRouteStatic.Yangify, Ip_Route_Vrf_Impl1.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_Vrf_IpRouteStatic_Impl.Yangify, self).__init__(*args, **kwargs)
            #super(Ip_Route_Vrf_IpRouteStatic.Yangify, self).__init__(*args, **kwargs)
            super(Ip_Route_Vrf_Impl1.Yangify, self).__init__(*args, **kwargs)
            self.indent = ""
            self.cli_fmt      = "{prefix}/{mask} {out} tag {tag} description {description}"
            self.undo_cli_fmt = "no ip route {prefix}/{mask} {out}"
            #self.add_name = f"{self.()}"

        def pre_process(self):
            candidate_cli = self.extract_candidate_cli_data()
            command = self._stringify_add_to_list_command(candidate_cli)
            self.result.add_command(command)
            print("giang"*30)
            debug_line(f"@new-section <{command}>")

        def extract_cli_data2(self, cli_data):
            if 'next_hop_ip_add' in cli_data:
                cli_data['out'] = cli_data['next_hop_ip_add']
            elif 'out_if' in cli_data:
                cli_data['out'] = cli_data['out_if']
            cli_data['tag'] = cli_data['tag']
            cli_data['description'] = cli_data['description']

        @debug_function(log_enter=True, log_exit=True)
        def post_process(self):
            if self.result is None:
                candidate_cli = self.extract_candidate_cli_data()
                command = self._stringify_add_to_list_command(candidate_cli)
                self.root_result.pop_section(command)

    def __init__(self, *args, **kwargs):
        super(Ip_Route_Vrf_IpRouteStatic_Impl, self).__init__(*args, **kwargs)

    def gen_command_tag(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value)

    def gen_diff_command_tag(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value) 

    def gen_command_description(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value)

    def gen_diff_command_description(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value)

    def gen_command_metric(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(default)

    def gen_diff_command_metric(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(default)

    def gen_command_next_hop_ip_add(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value)

    def gen_diff_command_next_hop_ip_add(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value)

    def gen_command_out_if(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value)

    def gen_diff_command_out_if(self, value):
        if value:
            command = "".format(value)
        else:
            command = "".format(value)

class Ip_Route_Vrf_Impl(Ip_Route_Vrf):
    class Yangify(Ip_Route_Vrf.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_Vrf_Impl.Yangify, self).__init__(*args, **kwargs)
            self.cli_fmt = "if route vrf {name}"
            self.cli_exit = None
            self.name = self.cli_fmt

        @debug_function(log_enter=True, log_exit=True)
        def post_process(self):
            if self.result is None:
                candidate_cli = self.extract_candidate_cli_data()
                command = self._stringify_add_to_list_command(candidate_cli)
                self.root_result.pop_section(command)

    def __init__(self, *args, **kwargs):
        super(Ip_Route_Vrf_Impl, self).__init__(*args, **kwargs)
    ip_route_static = Ip_Route_Vrf_IpRouteStatic_Impl

class Ip_Route_Impl(Ip_Route):
    class Yangify(Ip_Route.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_Impl.Yangify, self).__init__(*args, **kwargs)
            self.cli_fmt = None
            self.submode_indent = ""
            self.cli_exit = "!"

        @debug_function(log_enter=True, log_exit=True)
        def pre_process(self):
            running_cli   = self.extract_running_cli_data()
            candidate_cli = self.extract_candidate_cli_data()
            if not self.running or not self.is_same_cli_cfg(candidate_cli, running_cli):
                if self.cli_fmt:
                    command = self.cli_fmt.format(**candidate_cli)
                    self.result.add_command(self.indent + command)

        @debug_function(log_enter=True, log_exit=True)
        def post_process(self):
            running_cli   = self.extract_running_cli_data()
            candidate_cli = self.extract_candidate_cli_data()
            if not self.running or not self.is_same_cli_cfg(candidate_cli, running_cli):
                if len(self.indent) == 0:
                    self.result.add_command(self.submode_indent + self.cli_exit)

    def __init__(self, *args, **kwargs):
        super(Ip_Route_Impl, self).__init__(*args, **kwargs)
    
    ip_route_static = Ip_Route_IpRouteStatic_Impl
    vrf = Ip_Route_Vrf_Impl
    vrf1 = Ip_Route_Vrf_Impl1

class Ip_Impl(Ip):
    class Yangify(Ip.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Impl.Yangify, self).__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(Ip_Impl, self).__init__(*args, **kwargs)
    route = Ip_Route_Impl