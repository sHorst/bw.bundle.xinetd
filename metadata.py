defaults = {}

# install xninetd
if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'xinetd': {'installed': True, },
        }
    }
