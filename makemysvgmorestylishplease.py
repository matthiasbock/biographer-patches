#!/usr/bin/python

#import sys

svg = open('ugly_er.svg').read()

#if '<style type="text/css"></style>' in svg:
#	print "Warning: empty stylesheet, probably you have a problem with colors in your picture'

svg = svg.replace('><', '>\n<')

#svg = svg.replace('<g>\n<g ', '<g ').replace('</g>\n</g>\n</svg>', '</g>\n</svg>')

a = '''
.statevariable {
	font-size: 10px;
}
'''
b = '''
.VariableValue{
    fill: none;
    stroke: black;
    }

.statevariable {
font-size: 10px;
    fill: none;
    stroke: black
}
.rect {
    fill: none;
    stroke: black;
}
'''

svg = svg.replace(a, b)

open('pretty.svg', 'w').write(svg)

print 'done.'
