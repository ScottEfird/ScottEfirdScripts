#!/usr/bin/perl
$filename = $ARGV[0];
open(fh, $filename)
   or die "Could not open file '$filename' $!"; 
@lines = <fh>;
@rev = reverse(@lines);
foreach $revLine (@rev){
	print $revLine;
}