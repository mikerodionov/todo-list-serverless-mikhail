import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

