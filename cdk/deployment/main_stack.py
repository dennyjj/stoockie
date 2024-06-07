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
            timeout=Duration.seconds(20),
            code=aws_lambda.DockerImageCode.from_image_asset("../package")
        )

        rule = aws_events.Rule(
            self, "StoockieRule",
            # Run at 07:00 UTC+8 every Tuesday to Saturday
            schedule=aws_events.Schedule.cron(minute="0", hour="23", week_day="MON-FRI"),
        )

        rule.add_target(aws_events_targets.LambdaFunction(lambda_))
