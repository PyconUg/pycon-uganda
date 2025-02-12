from import_export import resources
from .models import Proposal

class ProposalResource(resources.ModelResource):
    class Meta:
        model = Proposal
        fields = ('created_date', 'title', 'talk_type', 'talk_category', 'elevator_pitch', 'talk_abstract', 'link_to_preview_video_url', 'anything_else_you_want_to_tell_us')
        export_order = ('created_date', 'title', 'talk_type', 'talk_category', 'elevator_pitch', 'talk_abstract', 'link_to_preview_video_url', 'anything_else_you_want_to_tell_us')