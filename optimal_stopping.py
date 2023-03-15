"""
Estimates the optimal plan for job search

Uses the Optimal Stopping Algorithm to identify the 
optimum trade-off between searching and pursuing job 
opportunities. The optimal cutoff is 1/e, which means
we reject the first (1/e) percent of jobs immediately
but rank order the selected, then accept the job 
that is of higher rank than those rejected

"""

import math
import helpers
import argparse

logger = helpers.set_up_logging()

OPTIMAL_CUTOFF = 1 / math.exp(1)
logger.info('Set optimal cutoff value at: {}'.format(OPTIMAL_CUTOFF))


def optimum_stopping(decision_time):
    """optimum stopping given  a time to decide

    Args:
        decision_time(int): integer representing the days/hours/etc. by when 
            decision has be made

    Returns: 
        explore_exploit(dict): a dictionary containing two values
            explore - means no commitment for this period of time
            exploit - after explore commit to choice that outranks
                rejected choices during explore stage
    """
    explore = round(decision_time * OPTIMAL_CUTOFF)
    exploit = round(decision_time - explore)
    explore_exploit = {'explore': explore, 'exploit': exploit}
    logger.info('Explore vs. Exploit set at: {}'.format(explore_exploit))

    return explore_exploit

def main(decision_time,num_of_stages):
    main_process = optimum_stopping(decision_time)
    main_explore = main_process['explore']
    logger.info('Explore phase for project: {0}'.format(main_explore))
    stages = {}
    stage_length = decision_time / num_of_stages
    logger.info('Each stage is approximately {} units long'.format(stage_length))
    for step in range(1,num_of_stages):
        stages['stage_{}'.format(step)] = optimum_stopping(stage_length)
    logger.info('Stages of Projects are: {}'.format(stages))
    return None



if __name__ == "__main__":
    #argument parser and documentation
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("decision_time", help="Absolute final deadline for entire search")
    parser.add_argument('num_of_stages', help='Number of stages in the project')
    args = parser.parse_args()
    
    #main function
    main(decision_time=int(args.decision_time), num_of_stages=int(args.num_of_stages))
