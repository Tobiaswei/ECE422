#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """          yZh,oOc�c���=K(�*�aS&P�8�o
 ��	��]#��g
�b��]'�;�N��Nҷ�6��N�`�GS3�[����vg���yc��x=��'rQ�T~hfFz�xa|�D�qΓz����X$M�
"""
from hashlib import sha256
if sha256(blob).hexdigest() == "62e31526cd63a4949aafecb8cabd1ec79a41d4207b98047466df90c9e2c22292":
    print "I come in peace."
elif sha256(blob).hexdigest() == "2ad3e9594f104a5e4693c7316f217a7c7e6a2fb00f059aca48ce56bcfb0c6139":
    print "Prepare to be destroyed!"
