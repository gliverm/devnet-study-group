try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")

# This does not work because except: must be last