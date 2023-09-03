import argparse
import json
import logging

import WazeRouteCalculator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calc_route(to_address, from_address, region="US", real_time=False):
    """
    Calculates commute time between two locations
    """
    commutes = []
    try:
        route = WazeRouteCalculator.WazeRouteCalculator(
            from_address, to_address, region
        )
        commutes.append(route.calc_route_info(real_time=real_time))
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        commutes.append({"distance": 0, "time": 0})

    return json.dumps(commutes)


def main():
    parser = argparse.ArgumentParser(
        description="Calculates the miles and average COMMUTE times between two addresses"
    )
    parser.add_argument("to_address", type=str, help="Destination address")
    parser.add_argument("from_address", type=str, help="Source address")
    parser.add_argument(
        "--region", type=str, default="US", help="Region (default is US)"
    )
    parser.add_argument(
        "--real_time", action="store_true", help="Whether to use real-time data"
    )

    args = parser.parse_args()

    commute = calc_route(
        to_address=args.to_address,
        from_address=args.from_address,
        region=args.region,
        real_time=args.real_time,
    )

    logger.info("Calculating route...")
    print(commute)


if __name__ == "__main__":
    main()
