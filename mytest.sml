local

  fun assertEq show x y =
    if x <> y then raise (Fail ("expected " ^ (show x) ^ " to equal " ^ (show y)))
    else OS.Process.success

  fun assertEqI x y = assertEq Int.toString x y

  fun printLn x = print (x ^ "\n")

  val tests = [
    ( "test_2_equals_2", (fn _ => assertEqI 2 2) ),
    ( "test_4_equals_4", (fn _ => assertEqI 4 4) )
  ]

  fun testRunner [] = (printLn "SUCCESS"; OS.Process.success)
    | testRunner ((name, body) :: remaining) =
      (print (name ^ ": ");
       body ();
       print "OK\n";
       testRunner remaining)

  fun testMain _ =
    (testRunner tests)
    handle e => (printLn ("FAIL\n" ^ ("Uncaught exception: " ^ (exnMessage e)));
                 OS.Process.failure)

in

  structure MyTest = struct
    fun main _ = testMain ()
  end

end
