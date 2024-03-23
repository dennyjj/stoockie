#!/usr/bin/env python3
import os

import aws_cdk as cdk
from deployment.main_stack import MainStack

app = cdk.App()
MainStack(app, "dennisbb",
          env=cdk.Environment(account=os.getenv('CDK_ACCOUNT'), region=os.getenv('CDK_REGION')))

app.synth()
