import aws_cdk as core
import aws_cdk.assertions as assertions

from deployment.main_stack import MainStack

def test_sqs_queue_created():
    app = core.App()
    stack = MainStack(app, "deployment")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
