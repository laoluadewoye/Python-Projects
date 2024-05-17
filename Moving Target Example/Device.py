from InfoConvert import *


class Packet:
    """
    A structured piece of level 2/3 data
    """
    def __init__(self, l3_data, l3_src, l3_dst):
        self.data = l3_data
        self.source = l3_src
        self.destination = l3_dst
        self.last_hop = None
        self.next_hop = None

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def set_last_hop(self, lh):
        self.last_hop = lh

    def set_next_hop(self, nh):
        self.next_hop = nh


class Interface:
    """
    A port on a device for level 2/3 communications
    """
    def __init__(self, label, inf_type, port_num, addr):
        self.label = label
        self.type = inf_type
        self.port = port_num
        self.ip_addr = addr

    def show_info(self):
        print(f'Interface {self.label} is a {self.type} on port {self.port} of the device.')
        print(f'Its address is {self.ip_addr}')


class Device:
    """
    Any type of device with communication abilities.
    Can be an endpoint or a network device.
    """

    def __init__(self, name, net_status=False, mtd_status=False):
        # Basic information
        self.name = name
        self.networking = net_status
        self.mtd = mtd_status

        # Packet tracking
        self.out_packets = []  # Tracking outbound packets
        self.in_packets = []  # Tracking inbound packets

        # Interface management
        self.interfaces = []  # Tracking interfaces of device
        self.v_infs = []

        # Routing management
        self.connections = {}  # Tracking connections to devices
        self.routing_table = {}
        self.device_table = {}  # Not needed by for simulation purposes

    def get_name(self):
        return self.name

    def set_interface(self, label, inf, addr):
        self.interfaces.append(Interface(label, inf, len(self.interfaces), get_working_ip(addr)))
        print(f'\nInterface {label} for {self.name} created.')

        if self.mtd:
            self.v_infs.append(
                Interface(label + '_v', inf, len(self.v_infs), get_working_ip(addr, mtd_status=self.mtd))
            )
            print(f'\nVirtual interface {label} for {self.name} created.')

    def get_interface(self):
        print("\nInterfaces of {}:".format(self.name))
        print("-----------------------------------")
        for interface in self.interfaces:
            interface.show_info()

        for interface in self.v_infs:
            interface.show_info()

    def check_request(self, asking_interface):
        ip_class = get_ip_class(asking_interface.ip_addr)

        # Chose interfaces to use
        if self.mtd:
            chosen_infs = self.v_infs
        else:
            chosen_infs = self.interfaces

        for inf in chosen_infs:
            q1_match = inf.ip_addr[0] == asking_interface.ip_addr[0]
            q2_match = inf.ip_addr[1] == asking_interface.ip_addr[1]
            q3_match = inf.ip_addr[2] == asking_interface.ip_addr[2]

            # Check if first quartets line up before doing a deeper match
            if (ip_class == 'A') and q1_match:
                return inf.ip_addr
            elif (ip_class == 'B') and q1_match and q2_match:
                return inf.ip_addr
            elif q1_match and q2_match and q3_match:
                return inf.ip_addr

        return None

    def confirm_connection(self, asking_name, ip_choice, asking_ip, other_device):
        print(f'{self.name} obtained the address {asking_ip} from {asking_name}')
        self.connections[asking_name] = (ip_choice, asking_ip)
        self.routing_table[asking_name] = asking_ip
        self.device_table[str(asking_ip)] = other_device

    def request_connection(self, other_device):
        # Check if connection already there
        od_name = other_device.get_name()
        exists = False

        for con in self.connections:
            if con[0] == od_name:
                print("Connection already exists.")
                exists = True

        # Set parameters
        dest_ip = None
        self_ip = None

        # Find a possible connection on the same network
        if not exists:
            for interface in self.interfaces:
                dest_ip = other_device.check_request(interface)
                if dest_ip is not None:
                    self_ip = interface.ip_addr
                    break

        # See if it worked
        if dest_ip is not None:
            # Add connection to record
            print(f'\n{self.name} obtained the address {dest_ip} from {od_name}')
            self.connections[od_name] = (self_ip, dest_ip)
            self.routing_table[od_name] = dest_ip
            self.device_table[str(dest_ip)] = other_device

            # Send information to other device
            other_device.confirm_connection(self.name, dest_ip, self_ip, self)
        else:
            print("New connection failed.")

    def choose_route(self, dst_name, dst_addr):
        # Check connections
        if dst_name in self.connections.keys():
            return dst_addr

        # Check routing table
        elif dst_name in self.routing_table.keys():
            return self.routing_table[dst_name]

        # Give the address of a routable device - not done for now
        return [127, 0, 0, 1]

    def accept_packet(self, pkt, dst_name):
        self.in_packets.append(pkt)

        # Chose interfaces to use
        if self.mtd:
            chosen_infs = self.v_infs
            print(f'Using Virtual Interface at {self.name} to accept packet.')
        else:
            chosen_infs = self.interfaces
            print(f'Using Hardware Interface at {self.name} to accept packet.')

        # Check to see if this is destination
        is_dest = False
        for inf in chosen_infs:
            if pkt.get_destination() == inf.ip_addr:
                is_dest = True

        if is_dest:
            print(pkt.data)
        else:
            self.send_packet(dst_name, pkt.data)

    def send_packet(self, dst_name, data):
        # Create the packet
        src = self.connections[dst_name][0]
        dst = self.connections[dst_name][1]
        pkt = Packet(data, src, dst)

        # Check routing table and connections to set prev and next
        next_hop = self.choose_route(dst_name, self.connections[dst_name][1])
        pkt.set_last_hop(self.connections[dst_name][0])
        pkt.set_next_hop(pkt)

        # Send packet
        print(f'\nSending a packet from {self.name} to {next_hop}.')
        self.out_packets.append(pkt)
        self.device_table[str(next_hop)].accept_packet(pkt, dst_name)


# Create one device
d1 = Device('Example One')
d1.set_interface('R2Two', 'Ethernet', '192.168.0.1')
d1.set_interface('R2Three', 'Ethernet', '192.168.1.1')
d1.get_interface()

# Create another
d2 = Device('Example Two')
d2.set_interface('Default', 'Ethernet', '192.168.0.2')
d2.get_interface()

# Create one last one, but with mtd mechanisms in place
d3 = Device('Example Three', mtd_status=True)
d3.set_interface('Default', 'Ethernet', '192.168.1.2')
d3.get_interface()

# Connect the three devices
d1.request_connection(d2)
d1.request_connection(d3)

# Send a packet
d1.send_packet('Example Two', 'It finally works!')
d1.send_packet('Example Three', 'It finally works!')
