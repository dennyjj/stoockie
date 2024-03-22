#!/usr/bin/env python3
import os

import aws_cdk as cdk
from deployment.deployment_stack import DeploymentStack

app = cdk.App()
DeploymentStack(app, "DeploymentStack",
                # env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
                env=cdk.Environment(account='074822175634', region='ap-southeast-1'))

app.synth()
