# doar argumente poziționale
def func(arg1, arg2):
    print("» arg1", arg1)
    print("» arg2", arg2)
func("ala", "bala")

# argumente poziționale și keyword arguments
def func(arg1, arg2, kwarg1="DEF1", kwarg2="DEF2"):
    print("» arg1", arg1)
    print("» arg2", arg2)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)

func("ala", "bala")
func("ala", "bala", "woot")
func("ala", "bala", "waat", "woot")
func("ala", "bala", kwarg2="waat", kwarg1="woot")
func(arg1="ala", arg2="bala", kwarg2="waat", kwarg1="woot")
func(kwarg2="waat", kwarg1="woot", arg1="ala", arg2="bala")

# capturăm orice extra-argument pozițional
def func(arg1, arg2, *args, kwarg1="DEF1", kwarg2="DEF2"):
    print("» arg1", arg1)
    print("» arg2", arg2)
    print("! args", args)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)

func("bala", kwarg2="waat", kwarg1="woot", arg1="ala")
func("ala", "bala", kwarg2="waat", kwarg1="woot")
func("ala", "bala", "ceva", "altceva", 7, 12 99, kwarg2="waat", kwarg1="woot")
func("ala", "bala", "ceva", "altceva", 7, 12, 99, kwarg2="waat", kwarg1="woot")

# unpacking de iterabil la apelarea funcției
lst = ["ala", "bala", "porto", "cala"]
func(*lst)
func("ala", "bala", "porto", "cala")
func("ala", "bala", "porto", "cala", kwarg1="my value!")

print("bla", "blu", sep=" !!! ")

# capturăm orice extra-keyword-arg
def func(arg1, arg2, *args, kwarg1="DEF1", kwarg2="DEF2", **kwargs):
    print("» arg1", arg1)
    print("» arg2", arg2)
    print("» args", args)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)
    print("» kwargs", kwargs)
func("ala", "bala", "porto", "cala", kwarg1="my value!", my_new_kwarg="WOW!")
func("ala", "bala", "porto", "cala", kwarg1="my value!", my_new_kwarg="WOW!", my_other_kwarg="AHA!")

# the * and the /

def func_with_required_keyword_arg(arg1, *, arg2):
    print(arg1)
    # sunt obligat să specific arg2
    # (pt. că nu are default)
    # dar pot să îl specific în call-ul funcției
    # doar ca kwarg!
    # (nu pot să îl scriu ca pozițional)
    print(arg2)
# func_with_required_keyword_arg("primul") # fails!
# func_with_required_keyword_arg("primul", "doiul")  # fails!
func_with_required_keyword_arg("primul", arg2="doiul") # ok!


def grep(src_filename, target_filename, /, *, pattern, insensitive=False, encoding="utf-8", src_encoding=None, target_encoding=None, buffer_size=4092):
    # the / says the args before can only be specified as positional
    pass

grep("/source/file.txt", "out/file.txt", pattern="POSIX") # works
# grep(src_filename="/source/file.txt", target_filename="out/file.txt", pattern="POSIX") # fails
