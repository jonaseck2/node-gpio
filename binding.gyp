{
    "targets": [{
        "target_name": "gpio",
        "sources": ["src/node-gpio.cpp", "src/GPIO.cpp", "src/PWM.cpp", "src/CapacitiveTouch.cpp"],
        'cflags': ['-fexceptions', "-std=c++0x"],
        'cflags_cc': ['-fexceptions'],
        "conditions": [
              [ 'OS=="mac"', {
                "xcode_settings": {
                    'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11','-stdlib=libc++'],
                    'OTHER_LDFLAGS': ['-stdlib=libc++'],
                    'MACOSX_DEPLOYMENT_TARGET': '10.7'
                }
            }]
        ]
    }]
}
