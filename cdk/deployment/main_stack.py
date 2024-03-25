from aws_cdk import (
    Duration,
    Stack,
    aws_lambda,
    aws_events,
    aws_events_targets
)
from constructs import Construct


class MainStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_ = aws_lambda.DockerImageFunction(
            self, "Stoockie",
            architecture=aws_lambda.Architecture.X86_64,
            timeout=Duration.seconds(10),
            code=aws_lambda.DockerImageCode.from_image_asset("../package")
        )

        rule = aws_events.Rule(
            self, "StoockieRule",
            schedule=aws_events.Schedule.cron(minute="0", hour="23", week_day="TUE-SAT"),
        )

        rule.add_target(aws_events_targets.LambdaFunction(lambda_))
