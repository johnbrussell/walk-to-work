from collections import namedtuple


Choice = namedtuple("Choice", ["name", "possibilities"])
Possibility = namedtuple("Possibility", ["description", "next_node", "min_wait", "max_wait", "probability"])
Result = namedtuple("Result", ["min_wait", "max_wait", "avg_wait", "probability"])


START = "Start"
END = "End"
DECISION_DICT = {
    START: [
        Choice(
            "Walk down the south side of Broadway to Technology Square (SW corner)",
            [Possibility("Walk down the south side of Broadway to Technology Square (SW corner)", "1", 0, 0, 1)]
        ),
    ],
    "1": [
        Choice(
            "Cross Technology Square",
            [
                Possibility("Cross Technology Square without waiting; go down Broadway to Galileo Galilei", "2", 0, 0,
                            5.0 / 18),
                Possibility("Wait to cross Technology Square; go down Broadway to Galileo Galilei", "3", 0, 65,
                            13.0 / 18),
            ]
        ),
        Choice(
            "Walk down Technology Square to Main and Vassar (NW corner)",
            [Possibility("Walk down Technology Square to Main and Vassar (NW corner)", "4", 24, 24, 1)]
        ),
    ],
    "2-3": [
        Choice("Walk down Galileo Galilei to Main and Vassar (NW corner)",
               [
                   Possibility("Walk down Galileo Galilei to Main and Vassar (NW corner)", "5", 9, 9, 1),
               ]),
        Choice("Cross Galileo Galilei",
               [
                Possibility("Cross Galileo Galilei without waiting", "6", 0, 0, 2.0 / 9),
                Possibility("Wait to cross Galileo Galilei", "7", 0, 70, 7.0 / 9),
                ]),
    ],
    "4-5": [
        Choice("Cross Main St", [
            Possibility("Cross Main St. without waiting", "8", 0, 0, 1.0 / 3),
            Possibility("Wait to cross Main St.", "9", 0, 60, 2.0 / 3),
        ]),
        Choice("Cross Galileo Galilei", [
            Possibility("Cross Galileo Galilei without waiting", "10", 0, 0, 1.0 / 3),
            Possibility("Wait to cross Galileo Galilei", "11", 0, 60, 2.0 / 3),
        ]),
        Choice("Cross diagonally to SE corner", [
            Possibility("Cross diagonally: no wait to cross Main", "32", 0, 30, 1.0 / 3),
            Possibility("Cross diagonally: no wait to cross Vassar", "33", 0, 30, 1.0 / 3),
            Possibility("Cross diagonally: wait, cross Main first", "34", 30, 45, 1.0 / 6),
            Possibility("Cross diagonally: wait, cross Vassar first", "35", 30, 45, 1.0 / 6),
        ])
    ],
    "6-7": [
        Choice("Walk down Galileo Galilei to Main and Vassar (NE corner)", [
            Possibility("Walk down Galileo Galilei to Main and Vassar (NE corner)", "12", 9, 9, 1),
        ]),
        Choice("Walk down Broadway to Ames (SW corner)", [
            Possibility("Walk down Broadway to Ames (SW corner)", "13", 0, 0, 1),
        ]),
    ],
    "8": [
        Choice("Cross Vassar", [
            Possibility("Wait to cross Vassar", "14", 0, 30, 1),
        ]),
    ],
    "9": [
        Choice("Cross Vassar", [
            Possibility("Wait to cross Vassar", "15", 30, 30, 1),
        ]),
    ],
    "10": [
        Choice("Cross Main St.", [
            Possibility("Wait to cross Main St.", "16", 0, 30, 1),
        ]),
        Choice("Walk down Main St. to Main and Ames (NW corner)", [
            Possibility("Walk down Main St. to Main and Ames (NW corner)", "17", 0, 0, 1),
        ]),
    ],
    "11": [
        Choice("Cross Main St.", [
            Possibility("Wait to cross Main St.", "18", 30, 30, 1),
        ]),
        Choice("Walk down Main St. to Main and Ames (NW corner)", [
            Possibility("Walk down Main St. to Main and Ames (NW corner)", "19", 0, 0, 1),
        ]),
    ],
    "12": [
        Choice("Cross Main St.", [
            Possibility("Cross Main St. without waiting", "20", 0, 0, 1.0 / 3),
            Possibility("Wait to cross Main St.", "21", 0, 60, 2.0 / 3),
        ]),
        Choice("Walk down Main St. to Main and Ames (NW corner)", [
            Possibility("Walk down Main St. to Main and Ames (NW corner)", "22", 0, 0, 1),
        ]),
    ],
    "13": [
        Choice("Walk down Ames St. to Main and Ames (NW corner)", [
            Possibility("Walk down Ames St. to Main and Ames (NW corner)", "23", 0, 0, 1),
        ]),
        Choice("Cross Ames St.", [
            Possibility("Cross Ames St. without waiting", "24", 0, 0, 5.0 / 18),
            Possibility("Wait to cross Ames St.", "25", 0, 65, 13.0 / 18),
        ]),
    ],
    "14-15-16-18-20-21-32-33-34-35": [
        Choice("Walk down Main St. to Main and Ames (SW corner)", [
            Possibility("Walk down Main St. to Main and Ames (SW corner)", "26", 0, 0, 1),
        ]),
    ],
    "17-19-22-23": [
        Choice("Cross Ames St.", [
            Possibility("Cross Ames St. without waiting", "27", 0, 0, 5.0 / 18),
            Possibility("Wait to cross Ames St.", "28", 0, 65, 13.0 / 18),
        ]),
        Choice("Cross Main St.", [
            Possibility("Cross Main St. without waiting", "29", 0, 0, 1.0 / 2),
            Possibility("Wait to cross Main St.", "30", 0, 45, 1.0 / 2),
        ]),
        Choice("Cross diagonally", [
            Possibility("Cross diagonally: no wait to cross Ames", END, 0, 25, 5.0 / 18),
            Possibility("Cross diagonally: no wait to cross Main", END, 10, 55, 1.0 / 2),
            Possibility("Cross diagonally: wait, cross Ames first", END, 25, 40, 3.0 / 18),
            Possibility("Cross diagonally: wait, cross Main first", END, 55, 60, 1.0 / 18),
        ])
    ],
    "24-25": [
        Choice("Walk down Ames St. to Main and Ames (NE corner)", [
            Possibility("Walk down Ames St. to Main and Ames (NE corner)", "31", 0, 0, 1),
        ]),
    ],
    "26": [
        Choice("Cross Ames St.", [
            Possibility("Cross Ames St. without waiting", END, 0, 0, 5.0 / 18),
            Possibility("Wait to cross Ames St.", END, 0, 65, 13.0 / 18),
        ]),
    ],
    "27": [
        Choice("Cross Main St.", [
            Possibility("Wait to cross Main St.", END, 0, 25, 1),
        ]),
    ],
    "28": [
        Choice("Cross Main St.", [
            Possibility("Wait to cross Main St.", END, 25, 25, 1),
        ]),
    ],
    "29": [
        Choice("Cross Ames St.", [
            Possibility("Wait to cross Ames St.", END, 10, 55, 1),
        ]),
    ],
    "30": [
        Choice("Cross Ames St.", [
            Possibility("Wait to cross Ames St.", END, 55, 55, 1),
        ]),
    ],
    "31": [
        Choice("Cross Main St.", [
            Possibility("Cross Main St. without waiting", END, 0, 0, 1.0 / 2),
            Possibility("Wait to cross Main St.", END, 0, 45, 1.0 / 2),
        ])
    ]
}


def flatten_dict():
    flat_dict = dict()
    for key, choices in DECISION_DICT.items():
        for subkey in key.split("-"):
            for choice in choices:
                assert round(sum([possibility.probability for possibility in choice.possibilities]), 10) == 1
                assert all([possibility.next_node == END for possibility in choice.possibilities]) or \
                       not any([possibility.next_node == END for possibility in choice.possibilities])
            flat_dict[subkey] = choices
    return flat_dict


def expand_choices(choices, decision_dict, results_dict, running_min, running_max,
                   running_avg, running_probability, running_description):
    for choice in choices:
        for possibility in choice.possibilities:
            expand_possibility(possibility, decision_dict, results_dict, running_min, running_max, running_avg,
                               running_probability, running_description)


def expand_possibility(possibility, decision_dict, results_dict, running_min, running_max, running_avg,
                       running_probability, running_description):
    running_min += possibility.min_wait
    running_max += possibility.max_wait
    running_avg += (possibility.min_wait + possibility.max_wait) / 2
    running_probability *= possibility.probability
    running_description = ", ".join([running_description, possibility.description]) if running_description else \
        possibility.description

    if possibility.next_node == END:
        results_dict[running_description] = Result(running_min, running_max, running_avg, running_probability)
    else:
        expand_choices(decision_dict[possibility.next_node], decision_dict, results_dict, running_min, running_max,
                       running_avg, running_probability, running_description)


def fill_out_choice_results_dict(choice_id, choice_results_dict, decision_dict, eliminations_list):
    choices = decision_dict[choice_id]
    for choice in choices:
        for possibility in choice.possibilities:
            if possibility.next_node != END:
                fill_out_choice_results_dict(possibility.next_node, choice_results_dict, decision_dict,
                                             eliminations_list)

    for tpe in ["min", "max", "avg"]:
        if tpe not in choice_results_dict:
            choice_results_dict[tpe] = dict()
        if tpe not in eliminations_list:
            eliminations_list[tpe] = dict()
        for choice in choices:
            avg_min = min([(choice_results_dict[tpe][possibility.next_node].min_wait + possibility.min_wait)
                           for possibility in choice.possibilities])
            avg_max = max([(choice_results_dict[tpe][possibility.next_node].max_wait + possibility.max_wait)
                           for possibility in choice.possibilities])
            avg_wait = sum([(choice_results_dict[tpe][possibility.next_node].avg_wait +
                             possibility.min_wait / 2.0 + possibility.max_wait / 2.0) *
                            possibility.probability for possibility in choice.possibilities])
            probability = sum([possibility.probability for possibility in choice.possibilities])

            new_result = Result(avg_min, avg_max, avg_wait, round(probability, 10))
            if choice_id not in choice_results_dict[tpe]:
                choice_results_dict[tpe][choice_id] = new_result

            if tpe == "min":
                new_value = avg_min
                old_value = choice_results_dict[tpe][choice_id].min_wait
            elif tpe == "max":
                new_value = avg_max
                old_value = choice_results_dict[tpe][choice_id].max_wait
            else:
                new_value = avg_wait
                old_value = choice_results_dict[tpe][choice_id].avg_wait

            if new_value < old_value:
                choice_results_dict[tpe][choice_id] = new_result

            choice_results_dict[tpe][f"{choice_id}: {choice.name}"] = new_result

        if choice_id not in eliminations_list[tpe]:
            eliminations_list[tpe][choice_id] = []
        new_result = choice_results_dict[tpe][choice_id]
        all_results = {key: result for key, result in choice_results_dict[tpe].items() if
                       key.startswith(f"{choice_id}:")}
        eliminated_results = [key for key, result in all_results.items() if (result.min_wait > new_result.max_wait or
                              (result.min_wait > new_result.min_wait and result.max_wait > new_result.max_wait and
                               result.avg_wait > new_result.avg_wait)) and key not in eliminations_list[tpe][choice_id]]
        eliminations_list[tpe][choice_id].extend(eliminated_results)


def prune_eliminations_list(eliminations_list, decision_dict):
    for tpe, choice_dict in eliminations_list.items():
        choice_ids = [str(d) for d in sorted([int(c) for c in choice_dict.keys() if c not in [START, END]],
                                             reverse=True)]
        for choice_id in choice_ids:
            parents = []
            for c_id, choices in decision_dict.items():
                if any([[possibility.next_node == choice_id for possibility in c.possibilities] for c in choices]):
                    parents.append(c_id)
            if all([eliminations_list[tpe][parent] for parent in parents]):
                eliminations_list[tpe][choice_id] = []


def main():
    decision_dict = flatten_dict()
    possibility_results_dict = dict()
    choice_results_dict = dict()
    choice_results_dict["min"] = dict()
    choice_results_dict["min"][END] = Result(0, 0, 0, 1)
    choice_results_dict["max"] = dict()
    choice_results_dict["max"][END] = Result(0, 0, 0, 1)
    choice_results_dict["avg"] = dict()
    choice_results_dict["avg"][END] = Result(0, 0, 0, 1)
    eliminations_list = dict()

    start = decision_dict.get(START)
    expand_choices(start, decision_dict, possibility_results_dict, 0, 0, 0, 1, "")
    fill_out_choice_results_dict(START, choice_results_dict, decision_dict, eliminations_list)

    print("Possibilities:")
    for key, result in possibility_results_dict.items():
        print(key, result)

    print("Choices:")
    for tpe, results_dict in choice_results_dict.items():
        print(tpe)
        for key, result in results_dict.items():
            print(key, result)

    print("Eliminations:")
    prune_eliminations_list(eliminations_list, decision_dict)
    for tpe, choice_dict in eliminations_list.items():
        print(tpe)
        for choice_id, eliminations in choice_dict.items():
            if eliminations:
                print(choice_id, eliminations)


main()
