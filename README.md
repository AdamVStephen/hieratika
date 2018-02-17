# HOWTO
To startup the server, one of the invocations that works is :

python2.7 -m hieratika.wservermain -H 0.0.0.0 -p 7000 -i ../demo/server/psps/psps.distributed.ini

# TODO
-   Design and implement the concept of pulses (DAP) - NOT DONE
-   Create the statistics backend
-   Design and implement smart reference counter for libraries/schedules usage (in order to avoid deletion)
-   Allow users to organise schedules/libraries in folders.
-   Allow users to delete schedules/libraries.
-   Rename the page concept to configuration model/object - NOT DONE
-   Document the design - NOT DONE
-   Write unit tests for the server - NOT DONE
-   Port the sqlite backend - NOT DONE
-   Setup the unit testing infrastructure for the client - NOT DONE
-   Write unit tests for the client - NOT DONE
