import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey


class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'ekey_env_int_fqdn'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from internal FQDN'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.compatible_omodules = [

            'dkey_env_csharp_int_fqdn',
        ]

    def add_arguments(self):

        self.parser.add_argument('--ekey-int-fqdn',
                                dest='ekey_int_fqdn',
                                type=str,
                                required=False,
                                default=None,
                                help='Set encryption key to internal FQDN')


    def generate(self):

        assert self.args.ekey_int_fqdn is not None

        self.ekey_val = self.args.ekey_int_fqdn.encode()

        return {
            'val' : self.ekey_val,
            'len' : len(self.ekey_val),
            'options' : self.args.__dict__,
        }
