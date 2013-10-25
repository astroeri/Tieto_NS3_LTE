# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# def options(opt):
#     pass

# def configure(conf):
#     conf.check_nonfatal(header_name='stdint.h', define_name='HAVE_STDINT_H')

def build(bld):
    module = bld.create_ns3_module('tietons3lte', ['core'])
    module.source = [
        'model/tietons3lte.cc',
        'helper/tietons3lte-helper.cc',
        ]

    module_test = bld.create_ns3_module_test_library('tietons3lte')
    module_test.source = [
        'test/tietons3lte-test-suite.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'tietons3lte'
    headers.source = [
        'model/tietons3lte.h',
        'helper/tietons3lte-helper.h',
        ]

    if bld.env.ENABLE_EXAMPLES:
        bld.recurse('examples')

    # bld.ns3_python_bindings()

