#!/usr/bin/python

#import sys

svg = open('ugly.svg').read()

if '<style type="text/css"></style>' in svg:
	print "Warning: empty stylesheet, probably you have a problem with colors in your picture'

#svg = svg.replace('><', '>\n<')

#svg = svg.replace('<g>\n<g ', '<g ').replace('</g>\n</g>\n</svg>', '</g>\n</svg>')

open('pretty.svg', 'w').write(svg)

print 'done.'