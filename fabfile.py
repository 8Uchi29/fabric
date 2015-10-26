from ilogue.fexpect import expect, expecting, run

def uptime():
    run('uptime')

def python_ss():
    prompts = []
    prompts += expect('>>>', 'print \"Hello World\"')
    prompts += expect('>>>', 'exit()')

    with expecting(prompts):
        run('python:')

