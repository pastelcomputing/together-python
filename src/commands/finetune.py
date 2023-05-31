def finetune_args(parser):
    # Required key for any finetune operation
    # TODO get key from env var
    parser.add_argument("--key", "-k", help="Together API Key", type=str, required=True)

    finetune_subparser = parser.add_subparsers(dest="finetune")

    # Create_finetune
    create_finetune_parser = finetune_subparser.add_parser("create_finetune")
    create_finetune_parser.add_argument(
        "--training_file",
        "-t",
        help="The ID of an uploaded file that contains training data.",
        required=True,
        type=str,
    )
    create_finetune_parser.add_argument(
        "--validation_file",
        "-v",
        default=None,
        help="The ID of an uploaded file that contains validation data.",
        type=str,
    )
    create_finetune_parser.add_argument(
        "--model",
        "-m",
        default=None,
        help="The name of the base model to fine-tune.",
        type=str,
    )
    create_finetune_parser.add_argument(
        "--n_epochs",
        "-ne",
        default=4,
        help="The number of epochs to train the model for.",
        type=int,
    )
    create_finetune_parser.add_argument(
        "--batch_size",
        "-b",
        default=None,
        help="The batch size to use for training.",
        type=int,
    )
    create_finetune_parser.add_argument(
        "--learning_rate_multiplier",
        "-lrm",
        default=None,
        help="The learning rate multiplier to use for training.",
        type=float,
    )
    create_finetune_parser.add_argument(
        "--prompt_loss_weight",
        "-plw",
        default=0.01,
        help="The weight to use for loss on the prompt tokens.",
        type=float,
    )
    create_finetune_parser.add_argument(
        "--compute_classification_metrics",
        "-ccm",
        default=False,
        action="store_true",
        help="Calculate classification-specific metrics using the validation set.",
    )
    create_finetune_parser.add_argument(
        "--classification_n_classes",
        "-cnc",
        default=None,
        help="The number of classes in a classification task.",
        type=int,
    )
    create_finetune_parser.add_argument(
        "--classification_positive_class",
        "-cpc",
        default=None,
        help="The positive class in binary classification.",
        type=str,
    )
    create_finetune_parser.add_argument(
        "--classification_betas",
        "-cb",
        default=None,
        help="Calculate F-beta scores at the specified beta values.",
        type=list,
    )
    create_finetune_parser.add_argument(
        "--suffix",
        "-s",
        default=None,
        help="Up to 40 characters that will be added to your fine-tuned model name.",
        type=str,
    )
    # End of create_finetune

    # List_Finetune
    finetune_subparser.add_parser("list_finetune")
    retrieve_finetune_parser = finetune_subparser.add_parser("retrieve_finetune")
    retrieve_finetune_parser.add_argument(
        "--fine_tune_id",
        "-ft",
        default=None,
        help="Fine-tuning ID",
        type=str,
        required=True,
    )

    # Cancel Finetune
    cancel_finetune_parser = finetune_subparser.add_parser("cancel_finetune")
    cancel_finetune_parser.add_argument(
        "--fine_tune_id",
        "-ft",
        default=None,
        help="Fine-tuning ID",
        type=str,
        required=True,
    )

    # List finetune events
    list_finetune_events_parser = finetune_subparser.add_parser("list_finetune_events")
    list_finetune_events_parser.add_argument(
        "--fine_tune_id",
        "-ft",
        default=None,
        help="Fine-tuning ID",
        type=str,
        required=True,
    )

    # Delete finetune model
    delete_finetune_model_parser = finetune_subparser.add_parser(
        "delete_finetune_model"
    )
    delete_finetune_model_parser.add_argument(
        "--model",
        "-m",
        default=None,
        help="Model name",
        type=str,
        required=True,
    )

    return parser
