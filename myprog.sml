structure MyProg = struct
  fun main _ =
    (print "Hello, World!\n"; OS.Process.success)
end
