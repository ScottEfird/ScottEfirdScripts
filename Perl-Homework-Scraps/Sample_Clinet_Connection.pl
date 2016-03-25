#!/usr/bin/perl
use IO::Socket;
$server_port = 3012;
$server = IO::Socket::INET->new (LocalPort => $server_port, Type => SOCK_STREAM, Reuse=> 1, Listen => SOMAXCONN)
    or die "Failed to open port $server_port: $@\n";
$client = $server->accept(); 
$line = <$client>;
print "Connection from $line \n";
print CLIENT "Hi $line \n";
close $client; 
close $server;
