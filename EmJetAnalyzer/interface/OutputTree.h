#ifndef EmergingJetAnalysis_EmJetAnalyzer_OutputTree_h
#define EmergingJetAnalysis_EmJetAnalyzer_OutputTree_h

#include <vector>

#include "TTree.h"

using std::vector;

namespace emjet
{
  class OutputTree {
  public:
    OutputTree() { Init(); }
    void Init();

    void Branch(TTree* tree);

    // Generated by cog
    // Do NOT edit until "end"
    //[[[cog
    //import cog
    //import vars_EmJetAnalyzer as mod; mod.gen_OutputTree()
    //]]]
    int                     run                 ;
    int                     lumi                ;
    int                     event               ;
    int                     bx                  ;
    int                     nVtx                ;
    int                     nGoodVtx            ;
    int                     nTrueInt            ;
    float                   met_pt              ;
    float                   met_phi             ;
    int                     nTracks             ;
    float                   pv_x                ;
    float                   pv_y                ;
    float                   pv_z                ;
    float                   pv_xError           ;
    float                   pv_yError           ;
    float                   pv_zError           ;
    float                   pv_chi2             ;
    float                   pv_ndof             ;
    float                   pv_pt2sum           ;
    int                     pv_nTracks          ;
    int                     pdf_id1             ;
    int                     pdf_id2             ;
    float                   pdf_x1              ;
    float                   pdf_x2              ;
    float                   pdf_pdf1            ;
    float                   pdf_pdf2            ;
    float                   pdf_scalePDF        ;
    bool                    HLT_PFHT400         ;
    bool                    HLT_PFHT475         ;
    bool                    HLT_PFHT600         ;
    bool                    HLT_PFHT800         ;
    bool                    HLT_PFHT900         ;
    bool                    HLT_HT250           ;
    bool                    HLT_HT350           ;
    bool                    HLT_HT400           ;
    bool                    HLT_HT500           ;
    vector<int>             jet_index               ;
    vector<int>             jet_source              ;
    vector<float>           jet_pt                  ;
    vector<float>           jet_eta                 ;
    vector<float>           jet_phi                 ;
    vector<float>           jet_cef                 ;
    vector<float>           jet_nef                 ;
    vector<float>           jet_chf                 ;
    vector<float>           jet_nhf                 ;
    vector<float>           jet_pef                 ;
    vector<float>           jet_mef                 ;
    vector<int>             jet_missHits            ;
    vector<int>             jet_muonHits            ;
    vector<float>           jet_alphaMax            ;
    vector<int>             jet_nDarkPions          ;
    vector<int>             jet_nDarkGluons         ;
    vector<float>           jet_minDRDarkPion       ;
    vector<float>           jet_theta2D             ;
    vector<vector<int> >    track_index               ;
    vector<vector<int> >    track_source              ;
    vector<vector<int> >    track_jet_index           ;
    vector<vector<int> >    track_vertex_index        ;
    vector<vector<float> >  track_vertex_weight       ;
    vector<vector<int> >    track_nHitsInFrontOfVert  ;
    vector<vector<int> >    track_missHitsAfterVert   ;
    vector<vector<float> >  track_pt                  ;
    vector<vector<float> >  track_eta                 ;
    vector<vector<float> >  track_phi                 ;
    vector<vector<float> >  track_pca_r               ;
    vector<vector<float> >  track_pca_eta             ;
    vector<vector<float> >  track_pca_phi             ;
    vector<vector<int> >    track_quality             ;
    vector<vector<int> >    track_algo                ;
    vector<vector<int> >    track_originalAlgo        ;
    vector<vector<int> >    track_nHits               ;
    vector<vector<int> >    track_nMissInnerHits      ;
    vector<vector<int> >    track_nTrkLayers          ;
    vector<vector<int> >    track_nMissInnerTrkLayers ;
    vector<vector<int> >    track_nMissOuterTrkLayers ;
    vector<vector<int> >    track_nMissTrkLayers      ;
    vector<vector<int> >    track_nPxlLayers          ;
    vector<vector<int> >    track_nMissInnerPxlLayers ;
    vector<vector<int> >    track_nMissOuterPxlLayers ;
    vector<vector<int> >    track_nMissPxlLayers      ;
    vector<vector<float> >  track_ipXY                ;
    vector<vector<float> >  track_ipZ                 ;
    vector<vector<float> >  track_ipXYSig             ;
    vector<vector<float> >  track_dRToJetAxis         ;
    vector<vector<float> >  track_distanceToJet       ;
    vector<vector<int> >    vertex_index               ;
    vector<vector<int> >    vertex_source              ;
    vector<vector<int> >    vertex_jet_index           ;
    vector<vector<float> >  vertex_x                   ;
    vector<vector<float> >  vertex_y                   ;
    vector<vector<float> >  vertex_z                   ;
    vector<vector<float> >  vertex_xError              ;
    vector<vector<float> >  vertex_yError              ;
    vector<vector<float> >  vertex_zError              ;
    vector<vector<float> >  vertex_deltaR              ;
    vector<vector<float> >  vertex_Lxy                 ;
    vector<vector<float> >  vertex_mass                ;
    vector<vector<float> >  vertex_chi2                ;
    vector<vector<float> >  vertex_ndof                ;
    vector<vector<float> >  vertex_pt2sum              ;
    vector<int>             gp_index               ;
    vector<int>             gp_status              ;
    vector<int>             gp_pdgId               ;
    vector<int>             gp_charge              ;
    vector<float>           gp_mass                ;
    vector<float>           gp_pt                  ;
    vector<float>           gp_eta                 ;
    vector<float>           gp_phi                 ;
    vector<float>           gp_vx                  ;
    vector<float>           gp_vy                  ;
    vector<float>           gp_vz                  ;
    vector<float>           gp_min2Ddist           ;
    vector<float>           gp_min2Dsig            ;
    vector<float>           gp_min3Ddist           ;
    vector<float>           gp_min3Dsig            ;
    vector<float>           gp_minDeltaR           ;
    vector<float>           gp_matched2Ddist       ;
    vector<float>           gp_matched2Dsig        ;
    vector<float>           gp_matched3Ddist       ;
    vector<float>           gp_matched3Dsig        ;
    vector<float>           gp_matchedDeltaR       ;
    vector<int>             gp_Lxy                 ;
    vector<int>             gp_isDark              ;
    vector<int>             gp_nDaughters          ;
    vector<int>             gp_hasSMDaughter       ;
    vector<int>             gp_hasDarkMother       ;
    vector<int>             gp_hasDarkPionMother   ;
    vector<int>             gp_isTrackable         ;
    //[[[end]]]
  };
}

void
emjet::OutputTree::Init() {
  // Generated by cog
  // Do NOT edit until "end"
  //[[[cog
  //import cog
  //import vars_EmJetAnalyzer as mod; mod.gen_Init()
  //]]]
  run                 = -1;
  lumi                = -1;
  event               = -1;
  bx                  = -1;
  nVtx                = -1;
  nGoodVtx            = -1;
  nTrueInt            = -1;
  met_pt              = -1;
  met_phi             = -1;
  nTracks             = -1;
  pv_x                = -1;
  pv_y                = -1;
  pv_z                = -1;
  pv_xError           = -1;
  pv_yError           = -1;
  pv_zError           = -1;
  pv_chi2             = -1;
  pv_ndof             = -1;
  pv_pt2sum           = -1;
  pv_nTracks          = -1;
  pdf_id1             = -1;
  pdf_id2             = -1;
  pdf_x1              = -1;
  pdf_x2              = -1;
  pdf_pdf1            = -1;
  pdf_pdf2            = -1;
  pdf_scalePDF        = -1;
  HLT_PFHT400         = -1;
  HLT_PFHT475         = -1;
  HLT_PFHT600         = -1;
  HLT_PFHT800         = -1;
  HLT_PFHT900         = -1;
  HLT_HT250           = -1;
  HLT_HT350           = -1;
  HLT_HT400           = -1;
  HLT_HT500           = -1;
  jet_index               .clear();
  jet_source              .clear();
  jet_pt                  .clear();
  jet_eta                 .clear();
  jet_phi                 .clear();
  jet_cef                 .clear();
  jet_nef                 .clear();
  jet_chf                 .clear();
  jet_nhf                 .clear();
  jet_pef                 .clear();
  jet_mef                 .clear();
  jet_missHits            .clear();
  jet_muonHits            .clear();
  jet_alphaMax            .clear();
  jet_nDarkPions          .clear();
  jet_nDarkGluons         .clear();
  jet_minDRDarkPion       .clear();
  jet_theta2D             .clear();
  track_index               .clear();
  track_source              .clear();
  track_jet_index           .clear();
  track_vertex_index        .clear();
  track_vertex_weight       .clear();
  track_nHitsInFrontOfVert  .clear();
  track_missHitsAfterVert   .clear();
  track_pt                  .clear();
  track_eta                 .clear();
  track_phi                 .clear();
  track_pca_r               .clear();
  track_pca_eta             .clear();
  track_pca_phi             .clear();
  track_quality             .clear();
  track_algo                .clear();
  track_originalAlgo        .clear();
  track_nHits               .clear();
  track_nMissInnerHits      .clear();
  track_nTrkLayers          .clear();
  track_nMissInnerTrkLayers .clear();
  track_nMissOuterTrkLayers .clear();
  track_nMissTrkLayers      .clear();
  track_nPxlLayers          .clear();
  track_nMissInnerPxlLayers .clear();
  track_nMissOuterPxlLayers .clear();
  track_nMissPxlLayers      .clear();
  track_ipXY                .clear();
  track_ipZ                 .clear();
  track_ipXYSig             .clear();
  track_dRToJetAxis         .clear();
  track_distanceToJet       .clear();
  vertex_index               .clear();
  vertex_source              .clear();
  vertex_jet_index           .clear();
  vertex_x                   .clear();
  vertex_y                   .clear();
  vertex_z                   .clear();
  vertex_xError              .clear();
  vertex_yError              .clear();
  vertex_zError              .clear();
  vertex_deltaR              .clear();
  vertex_Lxy                 .clear();
  vertex_mass                .clear();
  vertex_chi2                .clear();
  vertex_ndof                .clear();
  vertex_pt2sum              .clear();
  gp_index               .clear();
  gp_status              .clear();
  gp_pdgId               .clear();
  gp_charge              .clear();
  gp_mass                .clear();
  gp_pt                  .clear();
  gp_eta                 .clear();
  gp_phi                 .clear();
  gp_vx                  .clear();
  gp_vy                  .clear();
  gp_vz                  .clear();
  gp_min2Ddist           .clear();
  gp_min2Dsig            .clear();
  gp_min3Ddist           .clear();
  gp_min3Dsig            .clear();
  gp_minDeltaR           .clear();
  gp_matched2Ddist       .clear();
  gp_matched2Dsig        .clear();
  gp_matched3Ddist       .clear();
  gp_matched3Dsig        .clear();
  gp_matchedDeltaR       .clear();
  gp_Lxy                 .clear();
  gp_isDark              .clear();
  gp_nDaughters          .clear();
  gp_hasSMDaughter       .clear();
  gp_hasDarkMother       .clear();
  gp_hasDarkPionMother   .clear();
  gp_isTrackable         .clear();
  //[[[end]]]
}

void
emjet::OutputTree::Branch(TTree* tree) {
#define BRANCH(tree, branch) (tree)->Branch(#branch, &branch);
  // Generated by cog
  // Do NOT edit until "end"
  //[[[cog
  //import cog
  //import vars_EmJetAnalyzer as mod; mod.gen_Branch()
  //]]]
  BRANCH(tree, run                 );
  BRANCH(tree, lumi                );
  BRANCH(tree, event               );
  BRANCH(tree, bx                  );
  BRANCH(tree, nVtx                );
  BRANCH(tree, nGoodVtx            );
  BRANCH(tree, nTrueInt            );
  BRANCH(tree, met_pt              );
  BRANCH(tree, met_phi             );
  BRANCH(tree, nTracks             );
  BRANCH(tree, pv_x                );
  BRANCH(tree, pv_y                );
  BRANCH(tree, pv_z                );
  BRANCH(tree, pv_xError           );
  BRANCH(tree, pv_yError           );
  BRANCH(tree, pv_zError           );
  BRANCH(tree, pv_chi2             );
  BRANCH(tree, pv_ndof             );
  BRANCH(tree, pv_pt2sum           );
  BRANCH(tree, pv_nTracks          );
  BRANCH(tree, pdf_id1             );
  BRANCH(tree, pdf_id2             );
  BRANCH(tree, pdf_x1              );
  BRANCH(tree, pdf_x2              );
  BRANCH(tree, pdf_pdf1            );
  BRANCH(tree, pdf_pdf2            );
  BRANCH(tree, pdf_scalePDF        );
  BRANCH(tree, HLT_PFHT400         );
  BRANCH(tree, HLT_PFHT475         );
  BRANCH(tree, HLT_PFHT600         );
  BRANCH(tree, HLT_PFHT800         );
  BRANCH(tree, HLT_PFHT900         );
  BRANCH(tree, HLT_HT250           );
  BRANCH(tree, HLT_HT350           );
  BRANCH(tree, HLT_HT400           );
  BRANCH(tree, HLT_HT500           );
  BRANCH(tree, jet_index               );
  BRANCH(tree, jet_source              );
  BRANCH(tree, jet_pt                  );
  BRANCH(tree, jet_eta                 );
  BRANCH(tree, jet_phi                 );
  BRANCH(tree, jet_cef                 );
  BRANCH(tree, jet_nef                 );
  BRANCH(tree, jet_chf                 );
  BRANCH(tree, jet_nhf                 );
  BRANCH(tree, jet_pef                 );
  BRANCH(tree, jet_mef                 );
  BRANCH(tree, jet_missHits            );
  BRANCH(tree, jet_muonHits            );
  BRANCH(tree, jet_alphaMax            );
  BRANCH(tree, jet_nDarkPions          );
  BRANCH(tree, jet_nDarkGluons         );
  BRANCH(tree, jet_minDRDarkPion       );
  BRANCH(tree, jet_theta2D             );
  BRANCH(tree, track_index               );
  BRANCH(tree, track_source              );
  BRANCH(tree, track_jet_index           );
  BRANCH(tree, track_vertex_index        );
  BRANCH(tree, track_vertex_weight       );
  BRANCH(tree, track_nHitsInFrontOfVert  );
  BRANCH(tree, track_missHitsAfterVert   );
  BRANCH(tree, track_pt                  );
  BRANCH(tree, track_eta                 );
  BRANCH(tree, track_phi                 );
  BRANCH(tree, track_pca_r               );
  BRANCH(tree, track_pca_eta             );
  BRANCH(tree, track_pca_phi             );
  BRANCH(tree, track_quality             );
  BRANCH(tree, track_algo                );
  BRANCH(tree, track_originalAlgo        );
  BRANCH(tree, track_nHits               );
  BRANCH(tree, track_nMissInnerHits      );
  BRANCH(tree, track_nTrkLayers          );
  BRANCH(tree, track_nMissInnerTrkLayers );
  BRANCH(tree, track_nMissOuterTrkLayers );
  BRANCH(tree, track_nMissTrkLayers      );
  BRANCH(tree, track_nPxlLayers          );
  BRANCH(tree, track_nMissInnerPxlLayers );
  BRANCH(tree, track_nMissOuterPxlLayers );
  BRANCH(tree, track_nMissPxlLayers      );
  BRANCH(tree, track_ipXY                );
  BRANCH(tree, track_ipZ                 );
  BRANCH(tree, track_ipXYSig             );
  BRANCH(tree, track_dRToJetAxis         );
  BRANCH(tree, track_distanceToJet       );
  BRANCH(tree, vertex_index               );
  BRANCH(tree, vertex_source              );
  BRANCH(tree, vertex_jet_index           );
  BRANCH(tree, vertex_x                   );
  BRANCH(tree, vertex_y                   );
  BRANCH(tree, vertex_z                   );
  BRANCH(tree, vertex_xError              );
  BRANCH(tree, vertex_yError              );
  BRANCH(tree, vertex_zError              );
  BRANCH(tree, vertex_deltaR              );
  BRANCH(tree, vertex_Lxy                 );
  BRANCH(tree, vertex_mass                );
  BRANCH(tree, vertex_chi2                );
  BRANCH(tree, vertex_ndof                );
  BRANCH(tree, vertex_pt2sum              );
  BRANCH(tree, gp_index               );
  BRANCH(tree, gp_status              );
  BRANCH(tree, gp_pdgId               );
  BRANCH(tree, gp_charge              );
  BRANCH(tree, gp_mass                );
  BRANCH(tree, gp_pt                  );
  BRANCH(tree, gp_eta                 );
  BRANCH(tree, gp_phi                 );
  BRANCH(tree, gp_vx                  );
  BRANCH(tree, gp_vy                  );
  BRANCH(tree, gp_vz                  );
  BRANCH(tree, gp_min2Ddist           );
  BRANCH(tree, gp_min2Dsig            );
  BRANCH(tree, gp_min3Ddist           );
  BRANCH(tree, gp_min3Dsig            );
  BRANCH(tree, gp_minDeltaR           );
  BRANCH(tree, gp_matched2Ddist       );
  BRANCH(tree, gp_matched2Dsig        );
  BRANCH(tree, gp_matched3Ddist       );
  BRANCH(tree, gp_matched3Dsig        );
  BRANCH(tree, gp_matchedDeltaR       );
  BRANCH(tree, gp_Lxy                 );
  BRANCH(tree, gp_isDark              );
  BRANCH(tree, gp_nDaughters          );
  BRANCH(tree, gp_hasSMDaughter       );
  BRANCH(tree, gp_hasDarkMother       );
  BRANCH(tree, gp_hasDarkPionMother   );
  BRANCH(tree, gp_isTrackable         );
  //[[[end]]]
}

// Insert new empty element in nested vector and returns pointer to the added element
template <typename T>
vector<T>&
make_new_element (vector< vector<T> > & vec) {
  vec.push_back( vector<T>() );
  return vec.back();
}


#endif