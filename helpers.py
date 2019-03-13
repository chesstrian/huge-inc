def _cast_arg(value):
    try:
        return int(value)
    except ValueError:
        return value


def run_command(canvas, line):
    _line = line.split(' ')

    command = _line.pop(0)
    arguments = map(_cast_arg, _line)

    if command == 'C':
        canvas.create_canvas(*arguments)
        canvas.render_canvas()
    elif command == 'L':
        canvas.create_line(*arguments)
        canvas.render_canvas()
    elif command == 'R':
        canvas.create_rectangle(*arguments)
        canvas.render_canvas()
    elif command == 'B':
        canvas.bucket_fill(*arguments)
        canvas.render_canvas()
