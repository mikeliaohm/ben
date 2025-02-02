import os
import os.path

from configparser import ConfigParser

from nn.player import BatchPlayer, BatchPlayerLefty
from nn.bid_info import BidInfo
from nn.leader import Leader
from nn.lead_singledummy import LeadSingleDummy
from nn.contract import Contract


class Models:

    def __init__(self, name, model_version, api, bidder_model, contract_model, binfo_model, lead_suit_model, lead_nt_model, sd_model, sd_model_no_lead, player_models, search_threshold, lead_threshold, no_search_threshold, eval_after_bid_count, lead_accept_nn, ns, ew, bba_ns, bba_ew, use_bba, lead_included, claim, double_dummy, lead_from_pips_nt, lead_from_pips_suit, min_opening_leads, sample_hands_for_review, use_biddingquality, use_biddingquality_in_eval, double_dummy_eval, opening_lead_included, use_probability, matchpoint, pimc_use_declaring, pimc_use_defending, pimc_wait, pimc_start_trick_declarer, pimc_start_trick_defender, pimc_constraints, pimc_constraints_each_trick, pimc_max_playout, pimc_autoplaysingleton, pimc_max_threads, pimc_trust_NN,
                 use_adjustment,
                 adjust_NN,
                 adjust_NN_Few_Samples,
                 adjust_XX,
                 adjust_X,
                 adjust_passout,
                 adjust_passout_negative,
                 adjust_min1,
                 adjust_min2,
                 adjust_min1_by,
                 adjust_min2_by
                 ):
        self.name = name
        self.model_version = model_version
        self.api = api
        self.bidder_model = bidder_model
        self.contract_model = contract_model
        self.binfo_model = binfo_model
        self.lead_suit_model = lead_suit_model
        self.lead_nt_model = lead_nt_model
        self.sd_model = sd_model
        self.sd_model_no_lead = sd_model_no_lead
        self.player_models = player_models
        self._lead_threshold = lead_threshold
        self._search_threshold = search_threshold
        self._no_search_threshold = no_search_threshold
        self.eval_after_bid_count = eval_after_bid_count
        self._lead_accept_nn = lead_accept_nn
        self.ns = ns
        self.ew = ew
        self.bba_ns = bba_ns
        self.bba_ew = bba_ew
        self.use_bba = use_bba
        self.lead_included = lead_included
        self.claim = claim
        self.double_dummy = double_dummy
        self.lead_from_pips_nt = lead_from_pips_nt
        self.lead_from_pips_suit = lead_from_pips_suit
        self.min_opening_leads = min_opening_leads
        self.sample_hands_for_review = sample_hands_for_review
        self.use_biddingquality = use_biddingquality
        self.use_biddingquality_in_eval = use_biddingquality_in_eval
        self.double_dummy_eval = double_dummy_eval
        self.opening_lead_included = opening_lead_included
        self.pimc_use_declaring = pimc_use_declaring
        self.pimc_use_defending = pimc_use_defending
        self.pimc_wait = pimc_wait
        self.pimc_start_trick_declarer = pimc_start_trick_declarer
        self.pimc_start_trick_defender = pimc_start_trick_defender
        self.pimc_constraints = pimc_constraints
        self.pimc_constraints_each_trick = pimc_constraints_each_trick
        self.pimc_max_playout = pimc_max_playout
        self.pimc_autoplaysingleton = pimc_autoplaysingleton
        self.use_probability = use_probability
        self.matchpoint = matchpoint
        self.pimc_max_threads = pimc_max_threads
        self.pimc_trust_NN = pimc_trust_NN
        self.use_adjustment = use_adjustment
        self.adjust_NN = adjust_NN
        self.adjust_NN_Few_Samples = adjust_NN_Few_Samples
        self.adjust_XX = adjust_XX
        self.adjust_X = adjust_X
        self.adjust_passout = adjust_passout
        self.adjust_passout_negative = adjust_passout_negative
        self.adjust_min1 = adjust_min1
        self.adjust_min2 = adjust_min2
        self.adjust_min1_by = adjust_min1_by
        self.adjust_min2_by = adjust_min2_by

    @classmethod
    def from_conf(cls, conf: ConfigParser, base_path=None) -> "Models":
        if base_path is None:
            base_path = os.getenv('BEN_HOME') or '..'
        name = conf.get('models', 'name', fallback="BEN")
        model_version = conf.getint('models', 'model_version', fallback=1)
        api = conf.getboolean('models', 'api', fallback=False)
        search_threshold = float(conf['bidding']['search_threshold'])
        no_search_threshold = conf.getfloat('bidding', 'no_search_threshold', fallback=1)
        eval_after_bid_count = conf.getint('bidding', 'eval_after_bid_count', fallback=12)
        use_biddingquality = conf.getboolean('bidding', 'use_biddingquality', fallback=False)
        use_probability = conf.getboolean('bidding', 'use_probability', fallback=False)
        sample_hands_for_review = conf.getint('sampling', 'sample_hands_for_review', fallback=200)
        lead_threshold = float(conf['lead']['lead_threshold'])
        lead_accept_nn = float(conf['lead']['lead_accept_nn'])
        min_opening_leads = conf.getint('lead', 'min_opening_leads', fallback=1)
        double_dummy = conf.getboolean('lead', 'double_dummy', fallback=False)
        lead_from_pips_nt = conf.get('lead', 'lead_from_pips_nt', fallback="random")
        lead_from_pips_suit = conf.get('lead', 'lead_from_pips_suit', fallback="random")
        use_bba = conf.getboolean('models', 'use_bba', fallback=False)
        matchpoint = conf.getboolean('models', 'matchpoint', fallback=False)
        lead_included = conf.getboolean('eval', 'lead_included', fallback=True)
        double_dummy_eval = conf.getboolean('eval', 'double_dummy_eval', fallback=False)
        claim = conf.getboolean('cardplay', 'claim', fallback=True)
        pimc_use_declaring = conf.getboolean('pimc', 'pimc_use_declaring', fallback=False)
        pimc_use_defending = conf.getboolean('pimc', 'pimc_use_defending', fallback=False)
        pimc_wait = conf.getfloat('pimc', 'pimc_wait', fallback=1)
        pimc_start_trick_declarer = conf.getfloat('pimc', 'pimc_start_trick_declarer', fallback=1)
        pimc_start_trick_defender = conf.getfloat('pimc', 'pimc_start_trick_defender', fallback=1)
        pimc_max_playout = conf.getfloat('pimc', 'pimc_max_playout', fallback=-1)
        pimc_constraints = conf.getboolean('pimc', 'pimc_constraints', fallback=False)
        pimc_constraints_each_trick = conf.getboolean('pimc', 'pimc_constraints_each_trick', fallback=False)
        pimc_autoplaysingleton = conf.getboolean('pimc', 'pimc_autoplaysingleton', fallback=False)
        pimc_max_threads = conf.getint('pimc', 'pimc_max_threads', fallback=-1)
        pimc_trust_NN = conf.getfloat('pimc', 'pimc_trust_NN', fallback=0)
        use_adjustment = conf.getboolean('adjustments', 'use_adjustment', fallback=True)
        adjust_NN = conf.getint('adjustments', 'adjust_NN', fallback=50)
        adjust_NN_Few_Samples = conf.getint('adjustments', 'adjust_NN_Few_Samples', fallback=500)
        adjust_XX = conf.getint('adjustments', 'adjust_XX', fallback=100)
        adjust_X = conf.getint('adjustments', 'adjust_X', fallback=100)
        adjust_passout = conf.getint('adjustments', 'adjust_passout', fallback=-100)
        adjust_passout_negative = conf.getint('adjustments', 'adjust_passout_negative', fallback=3)
        adjust_min1 = conf.getfloat('adjustments', 'adjust_min1', fallback=0.002)
        adjust_min2 = conf.getfloat('adjustments', 'adjust_min2', fallback=0.0002)
        adjust_min1_by = conf.getint('adjustments', 'adjust_min1_by', fallback=200)
        adjust_min2_by = conf.getint('adjustments', 'adjust_min2_by', fallback=200)

        opening_lead_included = conf.getboolean('cardplay', 'opening_lead_included', fallback=False)
        use_biddingquality_in_eval = conf.getboolean('cardplay', 'claim', fallback=False)
        if use_bba == True:
            bba_ns = float(conf['models']['bba_ns'])
            bba_ew = float(conf['models']['bba_ew'])
        else:
            bba_ns = -1
            bba_ew = -1
        player_names = ['lefty_nt', 'dummy_nt', 'righty_nt', 'decl_nt', 'lefty_suit', 'dummy_suit', 'righty_suit', 'decl_suit']
        if model_version == 0:
            ns = -1
            ew = -1
            from nn.bidder import Bidder
            bidder_model = Bidder('bidder', os.path.join(base_path, conf['bidding']['bidder']))
        else:
            ns = float(conf['models']['ns'])
            ew = float(conf['models']['ew'])
            from nn.bidderv2 import Bidder
            bidder_model = Bidder('bidder', os.path.join(base_path, conf['bidding']['bidder']))

        return cls(
            name=name,
            model_version=model_version,
            api=api,
            bidder_model=bidder_model,
            contract_model=Contract(os.path.join(base_path, conf['contract']['contract'])),
            binfo_model=BidInfo(os.path.join(base_path, conf['bidding']['info'])),
            lead_suit_model=Leader(os.path.join(base_path, conf['lead']['lead_suit'])),
            lead_nt_model=Leader(os.path.join(base_path, conf['lead']['lead_nt'])),
            sd_model=LeadSingleDummy(os.path.join(base_path, conf['eval']['lead_single_dummy'])),
            sd_model_no_lead=LeadSingleDummy(os.path.join(base_path, conf['eval']['no_lead_single_dummy'])),

            player_models=[
                BatchPlayerLefty(name, os.path.join(base_path, conf['cardplay'][name])) if 'lefty' in name and opening_lead_included == False else
                BatchPlayer(name, os.path.join(base_path, conf['cardplay'][name]))
                for name in player_names
            ],

            search_threshold=search_threshold,
            lead_threshold=lead_threshold,
            no_search_threshold=no_search_threshold,
            eval_after_bid_count=eval_after_bid_count,
            lead_accept_nn=lead_accept_nn,
            ns=ns,
            ew=ew,
            bba_ns=bba_ns,
            bba_ew=bba_ew,
            use_bba=use_bba,
            lead_included=lead_included,
            claim=claim,
            double_dummy=double_dummy,
            lead_from_pips_nt=lead_from_pips_nt,
            lead_from_pips_suit=lead_from_pips_suit,
            min_opening_leads=min_opening_leads,
            sample_hands_for_review=sample_hands_for_review,
            use_biddingquality=use_biddingquality,
            use_biddingquality_in_eval=use_biddingquality_in_eval,
            double_dummy_eval=double_dummy_eval,
            opening_lead_included=opening_lead_included,
            use_probability=use_probability,
            matchpoint=matchpoint,
            pimc_use_declaring=pimc_use_declaring,
            pimc_use_defending=pimc_use_defending,
            pimc_wait=pimc_wait,
            pimc_start_trick_declarer=pimc_start_trick_declarer,
            pimc_start_trick_defender=pimc_start_trick_defender,
            pimc_constraints=pimc_constraints,
            pimc_constraints_each_trick=pimc_constraints_each_trick,
            pimc_max_playout=pimc_max_playout,
            pimc_autoplaysingleton=pimc_autoplaysingleton,
            pimc_max_threads=pimc_max_threads,
            pimc_trust_NN=pimc_trust_NN,
            use_adjustment=use_adjustment,
            adjust_NN=adjust_NN,
            adjust_NN_Few_Samples=adjust_NN_Few_Samples,
            adjust_XX=adjust_XX,
            adjust_X=adjust_X,
            adjust_passout=adjust_passout,
            adjust_passout_negative=adjust_passout_negative,
            adjust_min1=adjust_min1,
            adjust_min2=adjust_min2,
            adjust_min1_by=adjust_min1_by,
            adjust_min2_by=adjust_min2_by
        )

    @property
    def search_threshold(self):
        return self._search_threshold

    @search_threshold.setter
    def search_threshold(self, value):
        self._search_threshold = value

    @property
    def no_search_threshold(self):
        return self._no_search_threshold

    @no_search_threshold.setter
    def no_search_threshold(self, value):
        self._no_search_threshold = value

    @property
    def lead_threshold(self):
        return self._lead_threshold

    @property
    def lead_accept_nn(self):
        return self._lead_accept_nn
